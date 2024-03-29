from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("author", "title", "content")

        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("author", "content")

        widgets = {
            "author": forms.TextInput(),
            "content": forms.Textarea(),
        }
