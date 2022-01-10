# #-*-coding:utf-8-*-
import pytest
from common.read_config import ReadConfig
from page.base_page import Basepage
from common.path import config_path


@pytest.fixture()
def test_token(cmdopt, request):
    seassion = Basepage()
    test_ip = ReadConfig(config_path, cmdopt)('ip')
    test_port = ReadConfig(config_path, cmdopt)('port')
    url = 'https://{}:{}/login'.format(test_ip, test_port)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    parm = 'username=17521016982&password=123456'
    respone = seassion.post(url, headers=headers, data=parm, verify=False)

    # sessiod = requests.utils.dict_from_cookiejar(respone.cookies)

    def close():
        seassion.close()

    request.addfinalizer(close)
    return seassion


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default='shulie.yaml', help="环境变量"
    )


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("--cmdopt")
