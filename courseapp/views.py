
from django.shortcuts import render, redirect
from . forms import LessonForm, QuizForm, BadgeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Lesson, Quiz, Badge

# Create your views here.
@login_required
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.author = request.user
            lesson.save()
            return redirect('home')
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form})

@login_required 
def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            return redirect('home')
    else:
        form = QuizForm()
    return render(request, 'add_quiz.html', {'form': form})

@login_required
def add_badge(request):
    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        if form.is_valid():
            badge = form.save(commit=False)
            badge.save()
            return redirect('home')
    else:
        form = BadgeForm()
    return render(request, 'add_badge.html', {'form': form})

@login_required
def dashboard(request):
    lessons = Lesson.objects.all()
    quizzes = Quiz.objects.all()
    badges = Badge.objects.all()
    return render(request, 'dashboard.html', {'lessons': lessons, 'quizzes': quizzes, 'badges': badges})

@login_required
def lesson(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson.html', {'lessons': lessons})

@login_required
def badge(request):
    badges = Badge.objects.all()
    return render(request, 'badge.html', {'badges': badges})

@login_required
def certificate(request):
    return render(request, 'certificate.html')

@login_required
def quizes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizes.html', {'quizzes': quizzes})

@login_required
def course_details(request):
    return render(request, 'course-details.html')
