from django import forms
from appBlog.models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'created_on']
        widgets = {  # Fixed 'widget' to 'widgets'
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'created_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
