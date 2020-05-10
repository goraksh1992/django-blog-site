from django import forms
from .models import PostModel


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        "rows": 5,
        "cols": 5,
        "placeholder": "Enter blog content"
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter blog title"
    }))

    class Meta:
        model = PostModel
        fields = ['title', 'content']
