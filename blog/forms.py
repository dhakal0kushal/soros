from django import forms
from . import models

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        exclude = ['owner']