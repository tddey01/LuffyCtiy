#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework import serializers
from Course import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        '''

        :param obj:
        :return:
        '''

        print(obj.price_policy.all())
        return obj.price_policy.all().order_by("price").first().price

    class Meta:
        model = models.Course
        fields = ["id", "title", "course_img", "brief", "level", "study_num", "price"]


class CourseDetailSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="course.get_level_display")
    study_num = serializers.IntegerField(source="course.study_num")

    course_outline = serializers.SerializerMethodField()

    def get_course_outline(self, obj):
        '''

        :param obj:
        :return:
        '''
        return [{"id": outline.id, "title": outline.title, "content": outline.content} for outline in
                obj.course_outline.all().order_by("order")]

    price_policy = serializers.SerializerMethodField()

    def get_price_policy(self, obj):
        '''

        :param obj:
        :return:
        '''
        return [{"id": price.id, "valid_price_display": price.get_valid_period_display(), "price": price.price} for
                price in obj.course.price_policy.all()]

    teachers = serializers.SerializerMethodField()

    def get_teachers(self, obj):
        '''

        :param obj:
        :return:
        '''
        return [{"id": teacher.id, "name": teacher.name} for teacher in obj.teachers.all()]

    recommend_courses = serializers.SerializerMethodField()

    def get_recommend_courses(self, obj):
        '''

        :param obj:
        :return:
        '''
        return [{"id": course.id, "title": course.title} for course in obj.recommend_courses.all()]

    class Meta:
        model = models.CourseDetail
        fields = ["id", "hours", "summary", "level", "study_num", "recommend_courses", "teachers",
                  "price_policy", "course_outline"]
