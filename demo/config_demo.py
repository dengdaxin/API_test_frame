# encoding:utf-8
# @author:ddx
# @time:2021/7/5 22:19

import configparser
import os

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path,'../conf/config.ini')

config = configparser.ConfigParser()
config.read(config_path,encoding='utf-8')
print(config.get('default','URL'))
