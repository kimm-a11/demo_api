# #-*-coding:utf-8-*-


import requests

class Basepage:
    def __init__(self):
        self.seassion = requests.session()

    @property
    def get(self) -> requests:
        return self.seassion.get

    @property
    def post(self) -> requests:
        return self.seassion.post

    def close(self):
        self.seassion.close()

