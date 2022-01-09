# #-*-coding:utf-8-*-
import requests
from requests import request
from page.page_demo.page_demo import Demo
import pytest
from common.config_yaml import *


class TestDemo:
    def test_demo(self, token):
        seassions = token
        # url = 'https://{}:{}/login'.format(ip, port)
        # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # parm = 'username=17521016982&password=123456'
        # respone = seassion.post(url, headers=headers, data=parm, verify=False)
        url = 'https://{}:{}/project/showMyProject'.format(ip, port)
        respone = seassions.get(url, verify=False)
        print(respone.status_code)
        print(respone.text)

