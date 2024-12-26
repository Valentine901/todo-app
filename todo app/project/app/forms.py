from django.forms import ModelForm
from .models import Todo
from django import forms
class TodoForm(ModelForm):
    name =forms.CharField(widget=forms.TextInput
                          (attrs={'class':'forms-control', 'placeholder':'Add tasks'}), label='')
    
    class Meta:
        model = Todo
        fields = ['name']
    