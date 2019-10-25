#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django.urls import path
from Login import views

urlpatterns = [
    path('register',views.RegisterView.as_view()),
]
