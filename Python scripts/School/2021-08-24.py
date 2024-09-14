import csv
"""Book1 = open('Book1.csv','r+')
x = csv.writer(Book1,delimiter=',')
Rows = [['Satvik',2,43],['Rachit',4,56],['Praharsha',30,39]]
x.writerows(Rows)
Book1.close()"""

Book1 = open('Book1.csv','r+',newline='\r\n')
x = csv.reader(Book1)
for i in x:
    print(i)
Book1.close()