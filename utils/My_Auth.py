#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

import redis
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from utils import redis_pool
from Course.models import Account

CONN = redis.Redis(connection_pool=redis_pool.POOL)


class LoginAuth(BaseAuthentication):

    def authenticate(self, request):
        '''
        HTTP_AUTHENTICATION
        从请求头中获取前端带过来的token
        去request 对比
        :param request:
        :return:
        '''
        token = request.META.get("HTTP_AUTHENTICATION", "")
        if not token:
            raise AuthenticationFailed('没有携带token')
        # 去request比对
        user_id = CONN.get(str(token))
        if user_id == None:
            raise AuthenticationFailed("token过期")
        user_obj = Account.objects.filter(id=user_id).first()
        return user_obj, token
