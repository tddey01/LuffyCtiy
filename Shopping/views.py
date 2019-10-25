from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils import Base_Response
from utils import My_Auth
from utils import redis_pool
from Course import models
import redis
import json

# Create your views here.
'''
# 前端传过来 course_id  price_policy_id
# 把购物车数据放入redis
{
    SHOPPINGCAR_USERID_COURSE_ID: {
        "id", 
        "title",
        "course_img",
        "price_policy_dict": {
            price_policy_id: "{valid_period,  price}"
            price_policy_id2: "{valid_period,  price}"
            price_policy_id3: "{valid_period,  price}"      
        },
        "default_price_policy_id": 1          
    }
}
'''
# SHOPPINGCAR_KEY = "SHOPPINGCAR_%s_%s"
# CONN = redis.Redis(connection_pool=redis_pool.POOL)

# class ShoppingCarView(APIView):
#     authentication_classes = [My_Auth.LoginAuth,]
#
#     def post(self,request):
#
#         '''
#          1, 获取前端传过来的数据以及user_id
#         # 2, 校验数据的合法性
#         # 2.1 校验课程id合法性
#         # 2.2 校验价格策略id是否合法
#         # 3，构建redisKEY
#         # 4，构建数据结构
#         # 5  写入redis
#         :param request:
#         :return:
#         '''
#
#         res = Base_Response.BaseResponse()
#
#         # 1, 获取前端传过来的数据以及user_id
#         course_id = request.data.get('course_id','')
#         price_policy_id = request.data.get('price_policy_id','')
#         user_id = request.user.pk
#
#         # 2, 校验数据的合法性
#         course_obj = models.Course.objects.filter(id=course_id).first()
#         if not course_obj:
#             res.code = 1040
#             res.error = '课程id不存在'
#             return  Response(res.dict)
#
#         # 2.2 校验价格策略id是否合法
#         price_policy_queryset = course_obj.price_policy.all()
#         price_policy_dict = {}
#         for price_policy in price_policy_queryset:
#             price_policy_dict[price_policy.id] = {
#                 "price": price_policy.price,
#                 "valid_period": price_policy.valid_period,
#                 "valid_period_display": price_policy.get_valid_period_display()
#             }
#
#         if price_policy_id not in price_policy_dict:
#             res.code = 1041
#             res.error = '价格策略id不合法'
#             return  Response(res.dict)
#
#         # 3，构建redisKEY
#         key = SHOPPINGCAR_KEY % (user_id,course_id)
#
#         # 4，构建数据结构
#         course_info = {
#             "id":course_obj.id,
#             "title":course_obj.title,
#             "course_img":course_obj.course_img,
#             "price_policy_dict":json.dumps(price_policy_dict,ensure_ascii=False),
#             "default_price_policy_id":price_policy_id
#         }
#         # 5  写入redis
#         CONN.hmset(key,course_info)
#         res.data = "加入购物成功"
#         return Response(res.dict)
SHOPPINGCAR_KEY = "SHOPPINGCAR_%s_%s"
CONN = redis.Redis(connection_pool=redis_pool.POOL)


class ShoppingCarView(APIView):
    authentication_classes = [My_Auth.LoginAuth, ]

    def post(self, request):
        res = Base_Response.BaseResponse()
        # 1, 获取前端传过来的数据以及user_id
        course_id = request.data.get("course_id", "")
        price_policy_id = request.data.get("price_policy_id", "")
        user_id = request.user.pk
        # 2, 校验数据的合法性
        # 2.1 校验课程id合法性
        course_obj = models.Course.objects.filter(id=course_id).first()
        if not course_obj:
            res.code = 1040
            res.error = "课程id不合法"
            return Response(res.dict)
        # 2.2 校验价格策略id是否合法
        price_policy_queryset = course_obj.price_policy.all()
        price_policy_dict = {}
        for price_policy in price_policy_queryset:
            price_policy_dict[price_policy.id] = {
                "price": price_policy.price,
                "valid_period": price_policy.valid_period,
                "valid_period_display": price_policy.get_valid_period_display()
            }
        if price_policy_id not in price_policy_dict:
            res.code = 1041
            res.error = "价格策略id不合法"
            return Response(res.dict)
        # 3，构建redisKEY
        key = SHOPPINGCAR_KEY % (user_id, course_id)
        # 4，构建数据结构
        course_info = {
            "id": course_obj.id,
            "title": course_obj.title,
            "course_img": str(course_obj.course_img),
            "price_policy_dict": json.dumps(price_policy_dict, ensure_ascii=False),
            "default_price_policy_id": price_policy_id
        }
        # 5  写入redis
        CONN.hmset(key, course_info)
        res.data = "加入购物车成功"
        return Response(res.dict)

    def get(self, request):
        '''
        # 1, 拼接redis key
        # 2, 去redis中读取数据
        # 2.1 匹配所有的keys
        # 3，构建数据结构展示
        :param request:
        :return:
        '''
        res = Base_Response.BaseResponse()
        # 1, 拼接redis key
        user_id = request.user.pk
        shopping_car_key = SHOPPINGCAR_KEY % (user_id, "*")
        # 2, 去redis中读取数据
        # 2.1 匹配所有的keys
        # 3，构建数据结构展示
        all_keys = CONN.scan_iter(shopping_car_key)
        ret = []
        for key in all_keys:
            ret.append(CONN.hgetall(key))
        res.data = ret
        return Response(res.dict)
