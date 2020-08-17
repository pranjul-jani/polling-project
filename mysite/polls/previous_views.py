from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.template import loader


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}

    # return HttpResponse(template.render(context, request))

    # render is actually a shortcut with request as first parameter, then the template name, then context is optional
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # similar function get_list_or_404, it uses filter instead of get
    question = get_object_or_404(Question, pk=question_id)

    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist ")

    """

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        # request.Post is a dictionary like object that lets you access submitted data by key name,
        # In this case request.POST['choice'] returns the id of the selected choice, as a string,
        # request.POST values are always strings
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # request.POST['choice'] will raise a KeyError if no choice is selected, This code checks for key error
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data / form submission, This prevents data from being posted twice if a user hits the back button

        # we are using the reverse(), This function helps avoid having to hard-code a url in the view function.
        # reverse call will return a string like 'polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))





























