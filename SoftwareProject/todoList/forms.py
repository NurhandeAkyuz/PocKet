from django import forms
from .models import Board,  Task

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['board_name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']

