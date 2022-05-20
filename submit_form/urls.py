from django.contrib import admin
from django.urls import path
from submit_form import views

urlpatterns = [
    path('', views.form, name='form'),
]
