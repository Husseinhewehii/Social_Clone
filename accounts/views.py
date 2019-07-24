from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms as f

class SignUp(CreateView):
    form_class = f.User_Create_Form
    success_url = reverse_lazy('login')

    template_name = 'accounts/signup.html'