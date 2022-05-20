from django import forms
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FormData(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

