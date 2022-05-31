from django import forms
from accounts.models import User
# model form for my yuser model 

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['full_name','email', 'phone_number', 'username','password'] 
    