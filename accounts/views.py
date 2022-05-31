from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.models import User
from accounts.forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class View_Profile(DetailView):
    template_name = 'accounts/view-profile.html'
    model = User

    pass 

class Edit_Profile(UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = User
    fields = ['full_name', 'email', 'phone_number', 'user_name', 'profile_picture']
    success_url = '/accounts/view-profile'
    
class Change_Password(TemplateView):
    template_name = 'accounts/change-password.html'
    pass

class Delete_Account(DeleteView):
    template_name = 'accounts/delete-account.html'
    model = User
    success_url = '/'
    pass

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

class Test_Home(LoginRequiredMixin, TemplateView ):
    template_name = 'accounts/index.html'

class Sign_Out(LogoutView):
    next = reverse_lazy('sign_in')