# encoding:utf-8
# @author:ddx
# @time:2021/7/3 15:13
import os
import xlrd
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../demo/data/test_data.xlsx')
excel = ExcelUtils(excel_path,'Sheet1')
sheet = excel.get_merged_cell_value(8,0)

sheet_list = []
for row in range(1,excel.get_row_count()):
    row_dict = {}
    row_dict['事件'] = excel.get_merged_cell_value(row,0)
    row_dict['步骤序号'] = excel.get_merged_cell_value(row, 1)
    row_dict['步骤操作'] = excel.get_merged_cell_value(row, 2)
    row_dict['完成情况'] = excel.get_merged_cell_value(row, 3)
    sheet_list.append(row_dict)

all_list = []
first_row = excel.sheet.row(0)
for row in range(1,excel.get_row_count()):
    row_dict = {}
    for col in range(0,excel.get_col_count()):
        row_dict[first_row[col].value] = excel.get_merged_cell_value(row,col)
    all_list.append(row_dict)
for i in all_list:
    print(i)