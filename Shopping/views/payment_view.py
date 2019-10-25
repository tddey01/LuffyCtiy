#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework.views import APIView
from  rest_framework.response import Response
from utils import  Base_Response
from utils import redis_pool
from utils import My_Auth
import  redis

CONN = redis.Redis(connection_pool=redis_pool.POOL)

class PaymentView(APIView):
    authentication_classes = [My_Auth.LoginAuth,]
    def post(self,request):
        pass
