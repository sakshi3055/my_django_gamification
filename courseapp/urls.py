from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('lesson', views.lesson, name='lesson'),
    path('badge', views.badge, name='badge'),
    path('certificate', views.certificate, name='certificate'),
    path('quizes', views.quizes, name='quizes'),
    path('course-details', views.course_details, name='course-details'),
]

api_urlpatterns = [
    path('api/dashboard', views.dashboard, name='api_dashboard'),
    path('api/lesson', views.lesson, name='api_lesson'),
    path('api/badge', views.badge, name='api_badge'),
    path('api/certificate', views.certificate, name='api_certificate'),
    path('api/quizes', views.quizes, name='api_quizes'),
    path('api/course-details', views.course_details, name='api_course-details'),
   
]