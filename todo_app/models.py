from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    status = (
        ('PENDING', 'pending'),
        ('IN PROGRESS', 'in progress'),
        ('COMPLETED', 'completed'),
    )


    task_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    task_status = models.CharField(max_length=50, choices=status, default="PENDING")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
 