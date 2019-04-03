from django.urls import path

from todo.views import TodoView

from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
]
