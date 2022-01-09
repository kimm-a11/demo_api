# #-*-coding:utf-8-*-
from common.path import *
import string
import yaml


class ReadConfig:
    def __init__(self, file_path, name: str):
        file = os.path.join(file_path, name)
        with open(file, mode='r', encoding='utf-8') as f:
            self.content = yaml.safe_load(f)

    def __getitem__(self, key):
        return self.content[key]

    def __call__(self, key):
        return self[key]


if __name__ == "__main__":
    print(ReadConfig(config_path, 'shulie.yaml')('ip'))

