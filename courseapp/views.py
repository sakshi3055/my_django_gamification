
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *

from django.conf import settings
from django.core.mail import send_mail

@login_required
def dashboard(request):
    completed_lessons = LessonCompletion.objects.filter(user=request.user).order_by('-completed_at')
    total_points = 0
    for lesson in completed_lessons:
        total_points += lesson.lesson.points
    badges_collected = BadgeAssignment.objects.filter(user=request.user).order_by('-assigned_at')
    quiz_completed = QuizCompletion.objects.filter(user=request.user).order_by('-completed_at')
    num_quiz = quiz_completed.count()
    num_badges = badges_collected.count()
    num_lessons = completed_lessons.count()
    ctx = {
        'total_points': total_points,
        'num_badges': num_badges,
        'num_lessons': num_lessons,
        'num_quiz': num_quiz,
        'badges_collected': badges_collected[:5],
        'quiz_completed': quiz_completed,
        'completed_lessons': completed_lessons
    }
    return render(request, 'dashboard.html', ctx)

  
@login_required
def lesson_list(request):
    lessons = Lesson.objects.all()
    user = request.user
    completed_lessons = LessonCompletion.objects.filter(user=user).values_list('lesson', flat=True) # get all completed lessons
    ctx = {
        'lessons': lessons,
        'completed_lessons': completed_lessons
    }
    return render(request, 'lesson_list.html', ctx)

@login_required
def lesson_view(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    ctx = {
        'lesson': lesson
    }
    return render(request, 'lesson_view.html', ctx)

@login_required
def lesson_completed(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    user = request.user
    # check if the user has attempted the quizzes for this lesson
    quizzes = Quiz.objects.filter(lesson=lesson)
    for quiz in quizzes:
        try:
            QuizCompletion.objects.get(user=user, quiz=quiz)
        except QuizCompletion.DoesNotExist:
            messages.error(request, 'You have not completed the quizzes for this lesson')
            return redirect('lesson')
    else:
        # complete the lesson
        completion = LessonCompletion.objects.create(user=user, lesson=lesson)
        completion.save()
        # assign badge if any
        if lesson.badge:
            badge = BadgeAssignment.objects.create(user=user, badge=lesson.badge)
            badge.save()
        messages.success(request, 'Lesson marked as completed')
        return redirect('lesson')

@login_required
def completed_lessons(request):
    lessons = LessonCompletion.objects.filter(user=request.user)
    ctx = {
        'lessons': lessons
    }
    return render(request, 'completed_lessons.html', ctx)

# all quizzes for a lesson
@login_required
def lesson_quiz_view(request, lid):
    lesson = get_object_or_404(Lesson, id=lid)
    quizzes = Quiz.objects.filter(lesson=lesson)
    ctx = {
        'lesson': lesson,
        'quizzes': quizzes
    }
    return render(request, 'lesson_quiz_view.html', ctx)


# single quiz view
@login_required
def quiz_view(request, lid, qid):
    lesson = get_object_or_404(Lesson, id=lid)
    quiz = get_object_or_404(Quiz, id=qid)
    ctx = {
        'lesson': lesson,
        'quiz': quiz
    }
    return render(request, 'quiz_view.html', ctx)

@login_required
def quiz_completed(request, lid, qid):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=qid)
        user = request.user
        score = 0
        correct_answer = quiz.correct_answer
        if request.POST.get('answer') == correct_answer:
            score = quiz.points
        completion = QuizCompletion.objects.create(user=user, quiz=quiz, score=score)
        completion.save()
        messages.success(request, 'Quiz completed')
        return redirect('lesson_quizzes', lid)
    else:
        messages.error(request, 'Invalid request')
        return redirect('quiz', lid, qid)   

@login_required
def badge_list(request):
    badges = Badge.objects.all()
    ctx = {
        'badges': badges
    }
    return render(request, 'badge_list.html', ctx)

@login_required
def badges_collected(request):
    badges = BadgeAssignment.objects.filter(user=request.user)
    ctx = {
        'badges': badges
    }
    return render(request, 'badges_collected.html', ctx)

@login_required
def badge_view(request, id):
    badge = get_object_or_404(Badge, id=id)
    # get lesson or quiz info of the badge
    if badge.lesson:
        lesson = badge.lesson
        ctx = {
            'badge': badge,
            'lesson': lesson
        }
        return render(request, 'badge_view.html', ctx)
    elif badge.quiz:
        quiz = badge.quiz
        ctx = {
            'badge': badge,
            'quiz': quiz
        }
        return render(request, 'badge_view.html', ctx)
    
@login_required
def certificate_view(request):
    user = request.user
    lessons = LessonCompletion.objects.filter(user=user)
    if lessons:
        ctx = {
            'user': user,
            'lessons': lessons
        }
        return render(request, 'certificate.html', ctx)
    else:
        messages.error(request, 'You have not completed any lessons')
        return redirect('dashboard')



