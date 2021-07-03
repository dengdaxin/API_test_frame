# encoding:utf-8
# @author:ddx
# @time:2021/7/3 10:07

import xlrd
import os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'data/test_data.xlsx')

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_index(0)
# for i in range(1,sheet.nrows):
#     print(sheet.cell_value(i,0))
# sheet.merged_cells   获取表格合并单元格的位置
merged = sheet.merged_cells  # 返回一个列表   起始行、结束行、起始列、结束列

row_index = 3; col_index = 0

for (rlow,rhigh,clow,chigh) in merged:  # 遍历表格中所有合并单元格位置信息
    if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
        if (col_index >= clow and col_index < chigh):  #列坐标判断
            # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
             cell_value = sheet.cell_value(rlow,clow)
#print(cell_value)

#
def get_merged_cell_value(row_index,col_index):
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                break
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

print(get_merged_cell_value(0,0))

for i in range(9):
    print(get_merged_cell_value(i,0))
