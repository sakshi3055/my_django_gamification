from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('lesson/list', views.lesson_list, name='lesson'),
    path('lesson/<int:id>/view', views.lesson_view, name='lesson_view'),
    path('lesson/<int:id>/completed', views.lesson_completed, name='lesson_completed'),
    path('lessons/completed', views.completed_lessons, name='completed_lessons'),
    path('lesson/<int:lid>/q/<int:qid>/view', views.quiz_view, name='quiz_view'),
    path('lesson/<int:lid>/q/<int:qid>/completed', views.quiz_completed, name='quiz_completed'),
    path('quizes/<int:lid>/list', views.lesson_quiz_view, name='lesson_quizzes'),
    path('badge/list', views.badge_list, name='badge_list'),
    path('badge/collected', views.badges_collected, name='badges_collected'),
    path('badge/<int:id>/view', views.badge_view, name='badge_view'),
    path('certificate', views.certificate_view, name='certificate'),
    # progress
    path('progress', views.progress, name='progress')
]

