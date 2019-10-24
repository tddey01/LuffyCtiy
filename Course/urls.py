#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.urls import path
from Course import views

urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('list', views.CourseView.as_view()),
    path('detail/<int:pk>', views.CourseDetailView.as_view()),
    path('chapter/<int:pk>', views.CourseChapterView.as_view()),

]
