#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from rest_framework import serializers
from Course import models
import  hashlib

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = "__all__"

    def create(self, validated_data):
        pwd = validated_data['pwd']
        pwd_salt = 'luffy_password' + pwd
        md5_str = hashlib.md5(pwd_salt.encode()).hexdigest()
        user_obj = models.Account.objects.create(username=validated_data['username'],pwd=md5_str)
        return  user_obj

