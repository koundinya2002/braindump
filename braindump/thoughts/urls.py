from django.urls import path
from . import views
from .views import AddView, DeleteView, EditView

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', AddView.as_view(), name="add"),
    path('delete/<int:pk>/', DeleteView.as_view(), name="delete"),
    path('edit-<int:pk>/', EditView.as_view(), name="edit"),
]