#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django.urls import path
from Login import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('test_auth', views.TestView.as_view()),
]
