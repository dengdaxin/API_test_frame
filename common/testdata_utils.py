# encoding:utf-8
# @author:ddx
# @time:2021/7/3 16:45
import os
from common.excel_utils import ExcelUtils
current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '../test_data/test_case_data.xlsx')

class TestDataUtils:

    def __init__(self,test_data_path = test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(test_data_path,'Sheet1').get_sheet_data_by_dict()

    def __get_testcase_data_dict(self):
        testcase_dict = {}
        for row_data in self.test_data:
            testcase_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return testcase_dict

    def def_testcase_list(self):
        testcase_list = []
        for key,value in self.__get_testcase_data_dict().items():
            testcase_dict = {}
            testcase_dict['case_name'] = key
            testcase_dict['case_info'] = value
            testcase_list.append(testcase_dict)
        return testcase_list

if __name__=='__main__':
    testdata = TestDataUtils()
    for i in testdata.def_testcase_list():
        print(i)