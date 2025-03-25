import xlrd

# Open an old Excel file
wb = xlrd.open_workbook("employees.xls")
sheet = wb.sheet_by_index(0)

# Read data
for row in range(sheet.nrows):
    print(sheet.row_values(row))