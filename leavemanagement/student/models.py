from django.db import models
from django.contrib.auth.models import User
from faculty.models import Faculty
from django.utils import timezone


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Application(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    docs = models.FileField(upload_to='applications')
    description = models.TextField(default='Medical')
    is_pending = models.BooleanField(default=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateProcessed = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    from_Date = models.DateField(default=timezone.now)
    to_Date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author.user.username 