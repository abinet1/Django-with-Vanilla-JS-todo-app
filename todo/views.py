from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from todo.forms import Todo_Form

from todo.models import Todo
# Create your views here.

class Home(LoginRequiredMixin , CreateView ):
    template_name = 'todo/index.html'
    form_class = Todo_Form

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'TODO App'
        context['task'] = Todo.objects.filter(user = self.request.user).order_by('-created_date')
        return context
    
class Add_Task(LoginRequiredMixin, View):  
    def post(self, request, *args, **kwargs):
        form = Todo_Form(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.instance.user = request.user
            form.save()
        return redirect(reverse_lazy('home'))

class Delete_Task(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = Todo_Form(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.instance.user = request.user
            form.save()
        return redirect(reverse_lazy('home'))

class Update_Task(LoginRequiredMixin, TemplateView):
    template_name = 'todo/index.html'
    
class Edit_Task(LoginRequiredMixin, TemplateView):
    template_name = 'todo/index.html'

class Filter_Tasks(LoginRequiredMixin, TemplateView):
    template_name = 'todo/index.html'