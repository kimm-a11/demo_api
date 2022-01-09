# #-*-coding:utf-8-*-
from os.path import dirname
import os

data_path = dirname(dirname(os.path.realpath(__file__)))

config_path = os.path.join(data_path, 'config')

test_case_path = os.path.join(data_path, 'test_case')

yaml_path = os.path.join(data_path, 'data')

yaml_demo = os.path.join(yaml_path, 'demo')
