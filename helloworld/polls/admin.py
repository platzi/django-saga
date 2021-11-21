from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline): 
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]
    # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
