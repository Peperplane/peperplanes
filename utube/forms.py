from django import forms
from . import models

class CantactForm(forms.ModelForm):
    name=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':' form-control',}))
    email=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':' form-control',}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':' form-control',}))
    image=forms.ImageField(required=False)

    class Meta:
        model=models.ContactUs
        fields=(
            'name',
            'email',
            'message',
            'image'
        )

class StoryConnectForm(forms.ModelForm):
    name=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':' form-control',}))
    email=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':' form-control',}))
    title=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':' form-control',}))
    subtittel=forms.CharField(max_length=30,required=False,
    widget=forms.TextInput(attrs={'class':' form-control',}))
    story=forms.CharField(widget=forms.Textarea(attrs={'class':' form-control',}))
    image=forms.ImageField(required=False)
    url=forms.CharField(max_length=150,required=False,
    widget=forms.TextInput(attrs={'class':' form-control',}))

    class Meta:
        model=models.StoryConnect
        fields=(
            'name',
            'email',
            'title',
            'subtittel',
            'story',
            'image',
            'url'
        )