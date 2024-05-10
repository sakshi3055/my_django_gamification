from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points = models.IntegerField()
    image = models.ImageField(upload_to='courseapp/')

    def __str__(self):
        return self.image.url

class Lesson(models.Model):
    LEVEL_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=100)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='courseapp/')
    badge = models.OneToOneField(Badge, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    

    
    
class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    points = models.IntegerField(default=10)
    completed = models.BooleanField(default=False)
    badge = models.OneToOneField(Badge, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.question
    
class QuizCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.quiz.lesson.title
    
class LessonCompletion(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.lesson.title
    
class BadgeAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.badge.name