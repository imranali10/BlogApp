from django import forms
from .models import Blog, Contact


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'desc', 'slug')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'desc')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How May We Help You?'}),

        }
