from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Añade un comentario...'}),
        }
        