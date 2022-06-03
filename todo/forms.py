from django import forms
from todo.models import Todo

class Todo_Form(forms.ModelForm):
    class Meta:
        model = Todo 

        fields = ['title', 'description', 'catagory', 'starting_date', 'do_data', 'notify_me']
