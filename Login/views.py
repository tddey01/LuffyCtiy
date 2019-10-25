from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Login import serializers
from utils import Base_Response


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
