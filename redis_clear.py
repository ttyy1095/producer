#coding=utf-8
import redis
import re
import unittest
r = redis.StrictRedis(host="192.168.7.114", port='6379', db=0)

# print r.sismember("clients:app_test","{3638fdcf-6051-481d-b2b7-6b160aceebe8};1430000")
#清空流ID，组ID
keys = r.keys()
find = re.compile('[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')
for key in keys:
    if ('{' in key) and ("}" in key):
        r.delete(key)

    if len(find.findall(key)) > 0:
         r.delete(key)
