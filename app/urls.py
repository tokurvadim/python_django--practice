from django.urls import path

from app.views import LoginTemplateView, MyLogoutView, IndexView

urlpatterns = [
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]