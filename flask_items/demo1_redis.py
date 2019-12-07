# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from redis import StrictRedis

def demo():
    sr = StrictRedis(host="127.0.0.1", port = 6379 ,db =0)
    try:
        result=sr.set('name','laowang')
        print(result)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    demo()
