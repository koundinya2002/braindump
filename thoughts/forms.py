from django import forms
from .models import Thoughts

class AddForm(forms.ModelForm):
    class Meta:
        model = Thoughts
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-contrl'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Thoughts
        fields = ('title', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-contrl'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }