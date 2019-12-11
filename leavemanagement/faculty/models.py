from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    DEPARTMENT = (
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('ME', 'ME'),
        ('Medical', 'Medical'),
        ('Dean', 'Dean')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=30, choices=DEPARTMENT)
    level = models.IntegerField(default=2)

    def __str__(self):
        return self.user.username