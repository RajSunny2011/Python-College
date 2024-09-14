import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               password="server",
                               database="hotel_mangement")

def checkin():
    cur = mydb.cursor()
    x = input('Enter Name: ')
    y = input('Enter Room Number: ')
    z = input('Enter Number of nights: ')
    c = "insert into guests(Name,Room,Nights) values ({},{},{})".format(x,y,z)
    cur.execute(c)
    mydb.commit()
    cur.close()
checkin()