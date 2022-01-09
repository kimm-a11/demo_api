# #-*-coding:utf-8-*-
import yaml
import string
from common.path import *


class ReadYaml:
    def __init__(self, dath_path, filename):
        file = os.path.join(dath_path, filename)
        with open(file, mode='r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
        self.content = content

    def __getitem__(self, key):
        return self.content[key]

    def __call__(self, key, index=0, default=False, excepted='expect'):
        value_data = self[key]
        value_data_index = value_data[index]
        template_data = string.Template(value_data_index)

        value_data.pop(index)
        if default:
            return [template_data.safe_substitute(**value) for value in value_data]
        return [(template_data.safe_substitute(**value), value[excepted]) for value in value_data]


if __name__ == "__main__":
    print(ReadYaml(yaml_demo, 'filter_l.yaml')('kyt'))



