from django.db import models
from django.contrib.auth.models import User


# Create your models here.
'''
class Question(models.Model):
    id = models.BigAutoField(help_text="Question ID", primary_key=True)
    title = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.text


class QuestionContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, default="")

    line = models.IntegerField(default=0)
    text = models.TextField(default="")

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, default="")

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    line = models.IntegerField(default=0)
    text = models.TextField(default="")

    def __str__(self):
        return self.text


class ModelAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, default="")

    line = models.IntegerField(default=0)
    text = models.TextField(default="")

    def __str__(self):
        return self.text
'''