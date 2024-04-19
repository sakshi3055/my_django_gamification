from django.urls import path
from . import views

urlpatterns = [
    path("s/login", views.student_login, name="slogin"),
    path("s/register", views.student_register, name="sregister"),
    path('logout', views.logout_view, name='logout'),
    path('profile/create', views.create_profile, name='create_profile'),
]