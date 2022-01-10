# #-*-coding:utf-8-*-
import requests
from requests import request
from page.page_demo.page_demo import Demo
import pytest
from common.read_config import ReadConfig
from common.path import config_path


class TestDemo:
    def test_demo(self, test_token,cmdopt):
        seassions = test_token
        test_ip = ReadConfig(config_path, cmdopt)('ip')
        test_port = ReadConfig(config_path, cmdopt)('port')
        url = 'https://{}:{}/project/showMyProject'.format(test_ip, test_port)
        print(test_ip)
        respone = seassions.get(url, verify=False)
        print(respone.status_code)
        print(respone.text)

