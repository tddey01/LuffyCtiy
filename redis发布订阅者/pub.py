#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
import  redis

#
conn = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)

#
conn.publish("gaoxin333", "哈哈哈")
