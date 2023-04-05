from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

import os
from uuid import uuid4
from datetime import datetime
from django.utils import timezone

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/', ymd_path, uuid_name])

class Write(models.Model):
    title = models.CharField(max_length=100, null=True)
    contents = models.TextField(null=True) 
    email = models.CharField(max_length=128, null=True)
    imgfile = models.ImageField(null=True, upload_to='', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploadedFile = models.FileField(null=True, blank=True, upload_to = "Uploaded Files/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return '{}'.format(self.title)
        


def date_upload_to(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return 'media/'.join(['/', ymd_path, uuid_name])


