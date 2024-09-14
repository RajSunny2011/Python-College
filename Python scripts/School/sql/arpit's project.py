import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password="server",database="air_resv", charset="utf8")
mycursor=mydb.cursor()

def registration():
    print("Enter personal details below")
    print()
    n=input("Enter the Name : ")
    age=int(input("Enter the age : "))
    sex=input("Enter the sex : ")
    print("Please enter travel details below")
    print()
    cid=int(input("Enter customer id  : "))
    dod=input("Enter the date of departure : ")
    doa=input("Enter the date of arrival : ")
    pod=input("Enter the place of departure : ")
    poa=input("Enter the place of arrival : ")
    l=[n,age,sex,cid,dod,doa,pod,poa]
    c="insert into registration values('{}',{},'{}',{},'{}','{}','{}','{}')".format(n,age,sex,cid,dod,doa,pod,poa)
    mycursor.execute(c)
    mydb.commit()
    print()
    print("Customer Info Added")
    
def ticketprice():
    I=[]
    cid=int(input("Enter Customer ID :"))
    I.append(cid)
    print()
    print("we have following options for you:")
    print("1 . First class        Rs.6000")
    print("2 . Business class     Rs.5000")
    print("3 . Economy class      Rs.4000")
    print()
    x=int(input("Enter your choice: "))
    print()
    n=int(input("Enter the number of passengers: "))
    print()
    if x==1:
        print("You have opted for First class.")
        ticket_price=6000*n
        I.append(ticket_price)
        print("Extra luggage charge Rs 1000 per Kg")
        y= int(input("Enter the wieght of extra luggage : "))
        luggage_price= y*1000
        print("your luggage bill : Rs" , luggage_price)
        I.append(luggage_price)
        print("your total bill: " ,ticket_price+luggage_price)
        total_price=ticket_price + luggage_price
        I.append(total_price)
        I.append("First class")
    elif x== 2:
        print("You have opted for Business class .")
        ticket_price=5000*n
        I.append(ticket_price)
        print("Extra luggage charge Rs 1000 per Kg")
        y= int(input("Enter the wieght of extra luggage : "))
        luggage_price= y*1000
        print("your luggage bill : Rs" , luggage_price)
        I.append(luggage_price)
        print("your total bill: " ,ticket_price+luggage_price)
        total_price=ticket_price + luggage_price
        I.append(total_price)
        I.append("Buisness Class")
    elif x==3:
        print("You have opted for Economy class :")
        ticket_price= 4000*n
        I.append(ticket_price)
        print("Extra luggage charge Rs 1000 per Kg")
        y= int(input("Enter the wieght of extra luggage : "))
        luggage_price= y*1000
        print("your luggage bill : Rs" , luggage_price)
        I.append(luggage_price)
        print("your total bill: " ,ticket_price+luggage_price)
        total_price=ticket_price + luggage_price
        I.append(total_price)
        I.append("Economy class")
    print(I)
    tkty=tuple(I)
    sql="insert into total_bill values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tkty)
    mydb.commit()
    
def display():
    sql="select * from REGISTRATION "
    mycursor.execute(sql)
    res=mycursor.fetchall()
    print ("the customer details are as follows:")
    for i in res:
        print(i)
        
def delete():
    x=int(input("Enter the customer ID to be deleted: "))
    x1="delete from registration where customer_id={}".format(x)
    x2="delete from total_bill where customer_id={}".format(x)
    mycursor.execute(x1)
    mycursor.execute(x2)
    
def modify():
    while True:
        print()
        print(" '1' for modify Date of departure  ")
        print(" '2' for modify Date of arrival ")
        print(" '3' for modify Place of departure")
        print(" '4' for modify Place of arrival")
        print(" '5' to change ticket type")
        print(" '6' to exit modify ")
        print()
        x=int(input("Enter : "))
        print()
        print()
        if x==1:
            cid=int(input("Enter the customer ID :"))
            x1=input("Enter the New date of departure :")
            c1="update registration set date_of_departure='{}' where customer_id={}".format(x1,cid)
            mycursor.execute(c1)
            mydb.commit()
        elif x==2:
                cid=int(input("Enter the customer ID :"))
                x1=input("Enter the New date of Arrival :")
                c1="update registration set date_of_arrival='{}' where customer_id={}".format(x1,cid)
                mycursor.execute(c1)
                mydb.commit()
        elif x==3:
                cid=int(input("Enter the customer ID :"))
                x1=input("Enter the New Place of departure :")
                c1="update registration set place_of_departure='{}' where customer_id={}".format(x1,cid)
                mycursor.execute(c1)
                mydb.commit()
        elif x==4:
                cid=int(input("Enter the customer ID :"))
                x1=input("Enter the New Place of Arrival :")
                c1="update registration set place_of_arrival='{}' where customer_id={}".format(x1,cid)
                mycursor.execute(c1)
                mydb.commit()
        elif x==5:
                mycursor.execute("delete from total_bill where customer_id={}".format(cid))
                ticketprice()
        elif x==6:
                print("Exit")
                print()
                break
            
def search():
    c=int(input("Enter the customer ID : "))
    mycursor.execute("Select * from registration where customer_id={}".format(c))
    a=mycursor.fetchall()
    mycursor.execute("Select * from total_bill where customer_id={}".format(c))
    b=mycursor.fetchall()
    for i in a:
        print("Customer ID        : ",i[3])
        print("Name               : ",i[0])
        print("Sex                : ",i[2])
        print("Date of departure  : ",i[4])
        print("Date of Arrival    : ",i[5])
        print("Place of departure : ",i[6])
        print("Place of Arrival   : ",i[7])
    for i in b:
        print("Total Ticket price : ",i[3])
        print("Type of seat:",i[4])
        
def Type():
    mycursor.execute("select r.customer_id,r.name,r.age,r.sex,t.type from registration r ,total_bill t where r.customer_id=t.customer_id Group By Type")
    a=mycursor.fetchall()
    f=[]
    b=[]
    e=[]
    for i in a:
        if i[4].upper()=="First class".upper():
            f.append(i)
        elif i[4].upper()=="Business Class".upper():
            b.appen(i)
        elif i[4].upper()=="Economy Class".upper():
            e.appen(i)
    print("For First Class Passengers ")
    print("Number of First Class Passengers :",len(f))
    if len(f)!=0:
        for i in f:
            print("Customer ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Sex : ",i[3])
    else :
        print(" NO passenger in First Class")
    print("For Bussiness Class Passengers ")
    print("Number of Bussiness Class Passengers :",len(f))
    if len(f)!=0:
        for i in f:
            print("Customer ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Sex : ",i[3])
    else :
        print(" NO passenger in Bussiness Class")
    
    print("For Economy Class Passengers ")
    print("Number of Economy Class Passengers :",len(f))
    if len(f)!=0:
        for i in f:
            print("Customer ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Sex : ",i[3])
    else :
        print(" NO passenger in Economy Class")
            
print("SACHDEVA GLOBAL SCHOOL")
print("ARPIT WADHWA ")
print("CLASS 12A")
while True :
    print("~~~~~~~~~AIR TICKET RESERVATION~~~~~~~~~~")
    print("Enter 1: to enter customer data")
    print("Enter 2: for ticket amount")
    print("Enter 3: display all details.")
    print("Enter 4: delete a customer")
    print("Enter 5: Modify")
    print("Enter 6: Search")
    print("Enter 7: To check the Type  of flight")
    print("Enter 0: to exit")
    userinput=int(input("Enter your choice:"))
    if userinput==1:
        registration()
    elif userinput==2:
        ticketprice()
    elif userinput==3:
        display()
    elif userinput==4:
        delete()
    elif userinput==5:
        modify()
    elif userinput==6:
        search()
    elif userinput==7:
        Type()
    elif userinput==0:
        print("*********THANK YOU ******************")
        break
    else:
        print("*******WRONG INPUT*********")