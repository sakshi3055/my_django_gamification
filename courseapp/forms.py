from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Lesson, Badge, Quiz

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'points', 'level', 'image']
        widgets = {
              "content": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="content"
              )
          }

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ['name', 'description', 'points', 'image']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'lesson', 'question', 'option1', 'option2', 'option3', 'option4', 'correct_answer', 'image']

