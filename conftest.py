# #-*-coding:utf-8-*-


import pytest
import requests
from common.config_yaml import *
from page.base_page import Basepage

@pytest.fixture()
def token(request):
    global seassion
    seassion = Basepage()
    url = 'https://{}:{}/login'.format(ip, port)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    parm = 'username=17521016982&password=123456'
    respone = seassion.post(url, headers=headers, data=parm, verify=False)
    # sessiod = requests.utils.dict_from_cookiejar(respone.cookies)

    def close():
        seassion.close()
    request.addfinalizer(close)
    return seassion
