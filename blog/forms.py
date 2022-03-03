from django import forms
from .models import BlogPost

# this is how I connect my models to be edited from the front end. really nice because i dont have to go back through url /admin

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost 
        fields = ('title', 'header', 'header_image', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Something catchy!'}),
            'header': forms.TextInput(attrs={'class': 'form-control',}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }