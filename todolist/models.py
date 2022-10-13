from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)
    title = models.TextField()
    description= models.TextField()

