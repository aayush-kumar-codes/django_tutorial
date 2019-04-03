from django.urls import path

from todo.views import TodoView

from . import views

urlpatterns = [
    path('', TodoView.as_view(), name='todo'),
    path('login', views.login),
    path('register', views.register),
]
