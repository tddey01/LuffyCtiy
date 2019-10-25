#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from Shopping import views

urlpatterns = [
path('shopping_car',views.ShoppingCarView.as_view()),
]