from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

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
    points = models.IntegerField()
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='courseapp/')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points = models.IntegerField()
    image = models.ImageField(upload_to='courseapp/')

    def __str__(self):
        return self.name
    

    
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='courseapp/')
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.name