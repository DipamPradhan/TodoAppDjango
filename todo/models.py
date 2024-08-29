from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    title = models.CharField(max_length=100)
    srno = models.AutoField(auto_created=True, primary_key=True)
    addedAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=LOW,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
