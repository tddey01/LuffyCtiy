#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from  Shopping.views import ShoppingCar
from  Shopping.views import payment_view
from  Shopping.views import settlement_view

urlpatterns = [
    path('shopping_car', ShoppingCar.ShoppingCarView.as_view()),
    path('settlement', settlement_view.SettlementView.as_view()),
    path('payment', payment_view.PaymentView.as_view()),
]
