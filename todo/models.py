from django.db import models

# Create your models here.
import datetime




class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    due_date = models.DateField(null=True)
    description = models.TextField(default="")
    is_complete = models.BooleanField(default=False)
    complete_percentage  = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
