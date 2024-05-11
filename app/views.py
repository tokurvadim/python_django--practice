from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginTemplateView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

    """def get_success_url(self) -> str:
        return reverse('index')"""
    


class MyLogoutView(LogoutView):
    """def get_next_page(self) -> str | None:
        return redirect('login')"""
    pass


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'


