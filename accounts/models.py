from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score1 = models.IntegerField(default="0", blank=True, null=True)
    score2 = models.IntegerField(default="0", blank=True, null=True)
    score3 = models.IntegerField(default="0", blank=True, null=True)
    score4 = models.IntegerField(default="0", blank=True, null=True)
    score5 = models.IntegerField(default="0", blank=True, null=True)
    score6 = models.IntegerField(default="0", blank=True, null=True)
    score7 = models.IntegerField(default="0", blank=True, null=True)
    score8 = models.IntegerField(default="0", blank=True, null=True)
    score9 = models.IntegerField(default="0", blank=True, null=True)
    score10 = models.IntegerField(default="0", blank=True, null=True)
    score11 = models.IntegerField(default="0", blank=True, null=True)
    score12 = models.IntegerField(default="0", blank=True, null=True)