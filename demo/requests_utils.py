# --coding:utf-8--
import ast
import jsonpath
import requests
from common.config_utils import config

class RequestsUtils():

    def __init__(self):
        self.host = config.url_path
        self.headers = {'ContentType':'application/json,charset=utf-8'}
        self.session = requests.session()
        self.variables = {}  # 存放临时变量

    def request(self,request_infos):
        request_type = request_infos['请求方式']
        if request_type == 'get':
            result = self.__get(request_infos)
        elif request_type == 'post':
            result = self.__post(request_infos)
        else:
            result = {'code':3,'result':'请求方式不支持'}
        return result

    def __get(self,get_infos):
        url = self.host + get_infos['请求地址']
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_infos['请求参数(get)']),
                                    )
        response.encoding = response.apparent_encoding
        if get_infos['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),get_infos['取值代码'])[0]
            self.variables[get_infos['传值变量']] = value

        result = {'code':0,
                  'response_reason':response.reason,
                  'response_code':response.status_code,
                  'response_headers':response.headers,
                  'response_body':response.text}
        return result

    def __post(self, post_infos):
        url = self.host + post_infos['请求地址']
        response = self.session.post(url=url,
                                    headers = self.headers,
                                    #params={'access_token':'47_9zAvZ3hW2CXYq5psox-Klo8-A3iESY6KJPaAusqoAl_zYXlBFVCsaBSCW_QBYMwCPmbhshC5gC_dFnwpCnrtRLbnprxnpfyuG5UxRccDnueBqII9ho9z9I198MI0yFWro2rvLAmuzZ9P-t4NAVWfAAANIJ'},
                                    params=ast.literal_eval(post_infos['请求参数(get)']),
                                    json = ast.literal_eval(post_infos['提交数据(post)'])
                                    )
        response.encoding = response.apparent_encoding
        if post_infos['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),post_infos['取值代码'])[0]
            self.variables[post_infos['传值变量']] = value
        result = {'code': 0,
                  'response_reason': response.reason,
                  'response_code': response.status_code,
                  'response_headers': response.headers,
                  'response_body': response.text}
        return result

    def request_by_step(self,step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code'] != 0:
                break
        return temp_result
if __name__=='__main__':
    get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确获取access_token接口', '用例是否执行': '是', '测试用例步骤': 'step01', '接口名称': '', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': "{'grant_type':'client_credential','appid':'wx95b88e450068c8d2','secret':'5b6d758ece15c636e2c0a16fe56a2d97'}", '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': ''}
    #print(RequestsUtils().request(get_info))
    post_infos={'测试用例编号': 'case01', '测试用例名称': '测试能否正确获取access_token接口', '用例是否执行': '是', '测试用例步骤': 'step01', '接口名称': '', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': "{'grant_type':'client_credential','appid':'wx95b88e450068c8d2','secret':'5b6d758ece15c636e2c0a16fe56a2d97'}", '提交数据(post)': '{"tag":{"name":"o9o9912121"}}', '取值方式': 'json取值', '传值变量': '', '取值代码': '', '期望结果类型': ''}
    print(RequestsUtils().request(post_infos))