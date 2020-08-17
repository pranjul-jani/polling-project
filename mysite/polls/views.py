from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    # The DetailView generic view expects the primary key value captured from the URL to be called "pk",
    # so we’ve changed question_id to pk for the generic views.

    # Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html;

    # default context_object_name is question_list but we are using latest_question_list,
    # therefore we are overriding the context_object_name
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # return the context_object_name
    def get_queryset(self):
        """
        this functions returns the Questions whose published date is less than or equal to current date
        it does not return future questions
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    # default context_object_name is question same as we have used in our templates
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        excludes any questions that are not published yet

        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You did not select a choice",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(pk,)))


