from django.urls import path
from . import views
from .views import UserRegisterView

urlpatterns = [
    path('', views.landing, name="landing"),
    path('register/', UserRegisterView.as_view(), name="register"),
]