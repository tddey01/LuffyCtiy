from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from Course import models
from Course import serializers

# Create your views here.

class CategoryView(APIView):

    def get(self,request):
        '''
        通过ORM操作获取所有的分类的数据
        利用序列化器去序列化我们的数据
        :param request:
        :return:   返回
        '''
        queryset = models.Category.objects.all()

        ser_obj = serializers.CategorySerializer(queryset,many=True)

        return Response(ser_obj.data)

class CourseView(APIView):

    def get(self,request):
        '''
        获取过滤条件中的分类ID
        根据分类获取kec
        序列化课程数据
        :param request:
        :return:
        '''
        category_id = request.query_params.get('category',0)
        if category_id == 0:
            queryset = models.Course.objects.all().order_by('order')
        else:
            queryset = models.Course.objects.filter(category_id=category_id).all().order_by('order')

        ser_obj = serializers.CourseSerializer(queryset, many=True)

        return Response(ser_obj.data)



class CourseDetailView(APIView):

    def get(self,request,pk):
        '''
        根据pk获取到课程详情对象
        序列化课程详情
        返回
        :param request:
        :param pk:
        :return:
        '''
        course_detail_obj = models.CourseDetail.objects.filter(course__id=pk).first()
        if not course_detail_obj:
            return  Response({'code':1001,'error':'你查下查询课程详情不存在'})
        ser_obj = serializers.CourseDetailSerializer(course_detail_obj)
        return  Response(ser_obj.data)