from django.contrib import admin
from .models import Lesson, Badge, Quiz, QuizCompletion, BadgeAssignment, LessonCompletion, LessonCategory,Certificate

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Badge)
admin.site.register(Quiz)
admin.site.register(QuizCompletion)
admin.site.register(BadgeAssignment)
admin.site.register(LessonCompletion)
admin.site.register(LessonCategory)
admin.site.register(Certificate)