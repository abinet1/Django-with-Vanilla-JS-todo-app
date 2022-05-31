from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.models import User

# Create your views here.

class View_Profile(DetailView):
    template_name = 'accounts/view_profile.html'
    model = User

    pass 

class Edit_Profile(UpdateView):
    template_name = 'accounts/edit_profile.html'
    model = User
    fields = ['full_name', 'email', 'phone_number', 'user_name', 'profile_picture']
    success_url = '/accounts/view_profile'
    
class Change_Password(TemplateView):
    template_name = 'accounts/change_password.html'
    pass

class Delete_Account(DeleteView):
    template_name = 'accounts/delete_account.html'
    model = User
    success_url = '/'
    pass

class Sign_Up(CreateView):
    template_name = 'accounts/sign_up.html'
    model = User
    fields = ['full_name', 'email', 'phone_number', 'user_name', 'password']
    success_url = '/accounts/sign_in'
    pass

class Sign_In(LoginView):
    template_name = 'accounts/sign_in.html'

class Sign_Out(LogoutView):
    pass