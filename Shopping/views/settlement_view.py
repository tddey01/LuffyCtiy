#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from rest_framework.views import APIView
from  rest_framework.response import Response
from utils import  Base_Response
from utils import redis_pool
from utils import My_Auth
import  redis

CONN = redis.Redis(connection_pool=redis_pool.POOL)
SETTLEMENT_KEY = "SETTLEMENT_%s_%s"
GLOBAL_COUPON_KEY = "GLOBAL_COUPON_%s"
"""
前端传过来数据 course_list
redis = {
    settlement_userid_courseid: {
            id, 课程id，
            title,
            course_img,
            valid_period_display,
            price,
            course_coupon_dict: {
                coupon_id: {优惠券信息}
                coupon_id2: {优惠券信息}
                coupon_id3: {优惠券信息}
            }
            # 默认不给你选  这个字段只有更新的时候才添加
            default_coupon_id: 1  
    }

    global_coupon_userid: {
        coupon_id: {优惠券信息}
        coupon_id2: {优惠券信息}
        coupon_id3: {优惠券信息},
        # 这个字段只有更新的时候才添加
        default_global_coupon_id: 1

    }

}
"""

class SettlementView(APIView):
    authentication_classes = [My_Auth.LoginAuth,]
    def post(self,request):
        pass
