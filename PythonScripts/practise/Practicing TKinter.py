import pandas as pd
import openpyxl

pdfile = pd.ExcelFile(r'C:\Users\gupta\Documents\book1.xlsx')
opfile = openpyxl.load_workbook(pdfile)
s = opfile.active
df = pd.read_excel(pdfile)

print(s['c17'].value)