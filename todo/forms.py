from django import forms
from .models import Tag 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'I\'ll do This today ',
                'aria-label' : 'Todo',
                'aria-describedby' : 'add-btn'
            }))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)