from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('staff', views.staff, name='staff'),
    path('user', views.user, name='user'),
]
