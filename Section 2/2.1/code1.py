import xlrd
book = xlrd.open_workbook('SampleSuperstore.xls')

print("The number of sheets in the above excel file are {}".format(book.nsheets))
print("The names of sheets in the above excel file are {}".format(book.sheet_names()))

sheet1 = book.sheet_by_name('People')
sheet2 = book.sheet_by_index(0)

for i in range(sheet1.nrows):
    print(sheet1.row(i))
    
