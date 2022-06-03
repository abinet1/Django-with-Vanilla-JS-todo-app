from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
import json
from accounts.models import User
from accounts.forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from random import randint

from core.config import Config

# Create your views here.

class View_Profile(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    model = User

class Edit_Profile(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = User
    fields = ['full_name', 'email', 'phone_number', 'username', 'profile_picture']

    def get_success_url(self):
        return reverse_lazy('view_profile', kwargs={'pk':self.kwargs['pk']})
         
class Change_Password(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/forget-password.html'

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        email = body.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'status': 'fail', 'message': 'Email not found'})
        config = Config()
        response = send_mail("TODO App - Password Reset", "Your password is: " + str(randint(100000, 999999)), config.get_email(), [email], fail_silently=False)
        if response==1:
            return JsonResponse({'status': 'success', 'message': 'Password reset link has been sent to your email'})
        else:
            return JsonResponse({'status': 'fail', 'message': 'Error sending email'})

class Delete_Account(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        request.user.is_delete = True
        request.user.save()
        return redirect(reverse_lazy('sign_out')) 

class Sign_Up(CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = UserForm
    success_url = reverse_lazy('sign_in')

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password'])
        form.save()
        return super().form_valid(form)

class Sign_In(LoginView):
    template_name = 'accounts/sign-in.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('test_home'))



class Sign_Out(LogoutView):
    next = reverse_lazy('sign_in')