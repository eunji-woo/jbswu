from django import forms
from .models import Write

class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ['title', 'contents', 'email', 'imgfile', 'uploadedFile']

        