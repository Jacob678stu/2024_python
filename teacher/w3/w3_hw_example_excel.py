import sys;   
import datetime
import openpyxl



def print_grade_list_data(grade_list_data):
        for i in range(len(grade_list_data)):
            print(grade_list_data[i][0], end='\t')
            for j in range(1, len(grade_list_data[i])):
                print(grade_list_data[i][j], end='\t')
            ## new line
            print()

workbook = openpyxl.load_workbook('grade_list.xlsx')

sheet_names = workbook.sheetnames
sheet_name=sheet_names[0]
sheet = workbook[sheet_name]
cell_range_pattern='c5:j12'
cell_range = sheet[cell_range_pattern]
grade_list_data = []

for row in cell_range:
    row_list = []
    for cell in row:        
        row_list.append(cell.value)
    grade_list_data.append(row_list)



print('\nRead Excel file and print the data:\n')
print_grade_list_data(grade_list_data)