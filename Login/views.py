from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Login import serializers
from utils import Base_Response
from utils import redis_pool
from Course import  models
import redis
import  uuid

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        '''
        序列化器做校验

        :param request:
        :return:
        '''

        print(request.data)
        res = Base_Response.BaseResponse()
        ser_obj = serializers.RegisterSerializer(data=request.data)

        if ser_obj.is_valid():
            ser_obj.save()
            res.data = ser_obj.data
        else:
            res.code = 1020
            res.error = ser_obj.errors
        return Response(res.dict)

class LoginView(APIView):

    def post(self,request):
        res = Base_Response.BaseResponse()
        username = request.data.get('username','')
        pwd = request.data.get('pwd','')
        user_obj = models.Account.objects.filter(username=username,pwd=pwd).first()
        if not user_obj:
            res.code = 1030
            res.error = '用户名或者密码错误'
            return Response(res.dict)
        # 用户登录成功生成一个token写入redis
        # 写入redis  token : user_id
        conn = redis.Redis(connection_pool=redis_pool.POOL)
        try:
            token = uuid.uuid4()
            # conn.set(str(token), user_obj.id, ex=10)
            conn.set(str(token),user_obj.id)
            res.data = token
        except Exception as e:
            print(e)
            res.code = 1031
            res.error = '创建令牌失败'
        return Response(res.dict)

