from django.contrib import admin
from .models import Question, Choice
# Register your models here.



# It’d be better if you could add a bunch of Choices directly when you create the Question object.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # order in which the fields will appear in the admin section
    # fields = ['question_text', 'pub_date']

    # sectional breakdown of the fields
    fieldsets = [
        ('Poll-Question details', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'] }),
    ]

    inlines = [ChoiceInline]

    # by default admin displays __str__ representation of the model but we can edit this
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # how to filter our objects
    list_filter = ['pub_date']

    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)