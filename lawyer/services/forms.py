from django import forms
#from django.forms.widgets import Textarea
from .models import Client, Post, Comment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = {'first_name', 'last_name', 'phone'}

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['text',]
