# #-*-coding:utf-8-*-

from common.read_config import ReadConfig
from common.path import *
filename = 'shulie.yaml'

ip = ReadConfig(config_path, filename)('ip')
port = ReadConfig(config_path, filename)('port')

