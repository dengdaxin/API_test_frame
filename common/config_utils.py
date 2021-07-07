# encoding:utf-8
# @author:ddx
# @time:2021/7/5 22:22
import os
import time
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path,'../conf/config.ini')

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding='utf-8')

    @property
    def url_path(self):
        '''获取url'''
        value = self.__conf.get('default','URL')
        return value

    @property
    def case_data_path(self):
        '''获取url'''
        value = self.__conf.get('path','CASE_DATA_PATH')
        return value

    @property
    def log_path(self):
        '''获取url'''
        value = self.__conf.get('path', 'LOG_PATH')
        return value

    @property
    def log_level(self):
        '''获取url'''
        value = self.__conf.get('log', 'LOG_LEVEL')
        return int(value)

config = ConfigUtils()

if __name__ == '__main__':
    print(config.log_level)