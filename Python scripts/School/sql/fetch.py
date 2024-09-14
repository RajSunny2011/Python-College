import mysql.connector as mysql
mydb = mysql.connect(host="127.0.0.1",
                     user="root",
                     password="server",
                     database="sql_test")
cur = mydb.cursor()
cur.execute('select * from products')
data = cur.fetchall()
print(data)
cur.close()