# --coding:utf-8--
import ast

import requests
from common.config_utils import config

class RequestsUtils():

    def __init__(self):
        self.host = config.url_path
        self.headers = {'ContentType':'application/json,charset=utf-8'}
        self.session = requests.session()

    def request(self,request_infos):
        if request_infos['请求方式'] == 'get':
            return self.get(request_infos)
        if request_infos['请求方式'] == 'post':
            return self.post(request_infos)


    def get(self,get_infos):
        url = self.host + get_infos['请求地址']
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_infos['请求参数(get)']),
                                    )
        response.encoding = response.apparent_encoding  #

        result = {'code':0,
                  'response_reason':response.reason,
                  'response_code':response.status_code,
                  'response_headers':response.headers,
                  'response_body':response.text}
        return result

    def post(self, post_infos):
        url = self.host + post_infos['请求地址']
        response = self.session.post(url=url,
                                    headers = self.headers,
                                    #params={'access_token':'47_cYUGFb87tPJdXLm1h9pzzVej0n7ZePhRkSv_A6qe7jKNdx88N2u55WmxRpwgiaNJPO-jboqw11edxcerFByMjCTxyLLuaQwSPgOkxwVUh26qBIhDZFD_hNlVIsM6Cnb8zYErhPKhz8yxRmSGDVHaACARJV'},
                                    params=ast.literal_eval(post_infos['请求参数(get)']),
                                    json = ast.literal_eval(post_infos['提交数据(post)'])
                                    )
        response.encoding = response.apparent_encoding  #
        print(response.text)
        result = {'code': 0,
                  'response_reason': response.reason,
                  'response_code': response.status_code,
                  'response_headers': response.headers,
                  'response_body': response.text}
        return result


if __name__=='__main__':
    get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确获取access_token接口', '用例是否执行': '是', '测试用例步骤': 'step01', '接口名称': '', '请求方式': '', '请求地址': '/cgi-bin/token', '请求参数(get)': "{'grant_type':'client_credential','appid':'wx95b88e450068c8d2','secret':'5b6d758ece15c636e2c0a16fe56a2d97'}", '提交数据（post）': '', '取值方式': '', '传值变量': '', '取值代码': '', '期望结果类型': ''}
    #print(RequestsUtils().get(get_info))
    post_infos={'测试用例编号': 'case01', '测试用例名称': '测试能否正确获取access_token接口', '用例是否执行': '是', '测试用例步骤': 'step01', '接口名称': '', '请求方式': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': "{'grant_type':'client_credential','appid':'wx95b88e450068c8d2','secret':'5b6d758ece15c636e2c0a16fe56a2d97'}", '提交数据(post)': '{"tag":{"name":"opiio12121"}}', '取值方式': '', '传值变量': '', '取值代码': '', '期望结果类型': ''}
    RequestsUtils().post(post_infos)