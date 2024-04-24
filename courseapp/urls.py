from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('courses', views.courses, name='courses'),
    path('courses/<int:course_id>', views.course, name='course'),
    path('courses/<int:course_id>/enroll', views.enroll, name='enroll'),
    path('courses/<int:course_id>/drop', views.drop, name='drop'),
    path('courses/<int:course_id>/add', views.add, name='add'),
    path('courses/<int:course_id>/remove', views.remove, name='remove'),
    path('courses/<int:course_id>/edit', views.edit, name='edit'),
    path('courses/<int:course_id>/delete', views.delete, name='delete'),
    path('courses/create', views.create, name='create'),
    path('courses/search', views.search, name='search'),
    path('courses/filtered', views.filtered, name='filtered'),
    path('courses/sort', views.sort, name='sort'),
    path('courses/sorted', views.sorted, name='sorted'),
    path('courses/filtered_sorted', views.filtered_sorted, name='filtered_sorted'),
    path('courses/filtered_sorted', views.filtered_sorted, name='filtered_sorted'),
    path('courses/<int:course_id>/lessons', views.lessons, name='lessons'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>', views.lesson, name='lesson'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/edit', views.edit_lesson, name='edit_lesson'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/delete', views.delete_lesson, name='delete_lesson'),
    path('courses/<int:course_id>/lessons/create', views.create_lesson, name='create_lesson'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/contents', views.contents, name='contents'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/contents/<int:content_id>', views.content, name='content'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/contents/<int:content_id>/edit', views.edit_content, name='edit_content'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/contents/<int:content_id>/delete', views.delete_content, name='delete_content'),

]