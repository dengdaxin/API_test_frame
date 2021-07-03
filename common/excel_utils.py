# encoding:utf-8
# @author:ddx
# @time:2021/7/3 12:14
import os
import xlrd

class ExcelUtils:
    def __init__(self,excel_path,sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet_data()  # 表格对象

    def get_sheet_data(self):
        workbook = xlrd.open_workbook(self.excel_path)
        sheet = workbook.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        '''获取行'''
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        '''获取列'''
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self,row_index,col_index):
        '''获取单元格的在值'''
        cell_value = self.sheet.cell_value(row_index,col_index)
        return cell_value

    def get_merged_info(self):
        '''获取表格中合并信息，返回的是一个列表：起始行、结束行、起始列、结束列'''
        merged = self.sheet.merged_cells
        return merged

    def get_merged_cell_value(self,row_index, col_index):
        '''能获取单元格信息，也能获取合并单元格的信息'''
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_value(rlow, clow)
                    break
                else:
                    cell_value = self.__get_cell_value(row_index, col_index)
            else:
                cell_value = self.__get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_data_by_dict(self):
        '''将表格数据返回为列表字典类型'''
        all_data_list = []
        first_row = self.sheet.row(0)  # 获取首行数据
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../demo/data/test_data.xlsx')
    excel = ExcelUtils(excel_path,'Sheet1')
    print(excel.get_sheet_data_by_dict())