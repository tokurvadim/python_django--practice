from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView



class LoginTemplateView(LoginView):
    #redirect_authenticated_user = True
    template_name = 'login.html'

    """def get_success_url(self) -> str:
        return reverse('index')"""
    


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'



"""class VacationView(DetailView):
    model = None
    template_name = ''"""


