'''for key,value in dict.items():
    dict[key]:list(input("enter the name of "+key+" you want to purchase : ").split(",").captalize())
k=[]
for value in dict.items():
   for i in list:
        for keys,values in i.items():
            if value==keys:
                k=k.append(values)
print(k)'''
a="WELCOME TO ABC GROCERY STORE".center(168,"=")
print(a)

import sys
dict={"fruit":"","veg":"","rice_and_grains":"","dals":" ","dairy":" ","cookware": " ","snack_sweet":"",}
fruit= {"Mango":110, "Banana":50, "Apple":60, "Orange":40, "Grapes":50, "Guava":60, "Papaya":50,
        "Pineapple":60, "Watermelon":50, "Pomegranate":70, "Kiwi":80, "Lychee":80, "Strawberry":120,
        "Muskmelon":70, "Cantaloupe":40, "Sapota (Chikoo)":90, "Custard apple (Sitaphal)":80, "Jackfruit":40, "Avocado":130,
        "Dragonfruit":190, "Blueberries":70, "Raspberries":90, "Peach":70, "Pear":40,
        "Amla (Gooseberry)":50, "Passion fruit":80, "Jamun (Indian blackberry)":70,
        "Indian Gooseberry (Amla)":90, "Wood Apple (Bael)":50}
veg= {"Potato":40, "Tomato":40, "Onion":40, "Garlic":40, "Ginger":40, "Spinach":35,
      "Okra":55, "Eggplant":40, "Cauliflower":30, "Cabbage":30, "Green peas":40, "Bitter gourd":30,
      "Ridge gourd":40, "Bottle gourd":40, "Snake gourd":40, "Brinjal":30, "Carrot":35, "Beetroot":30, "Radish":35,
      "Turnip":35, "Cucumber":35, "Lettuce":30, "Green beans":30, "Cluster beans":45, "Fenugreek leaves":30,
      "Coriander leaves":35, "Curry leaves":25, "Mint leaves":25, "Green chili":25, "Red chili":35, "Bell pepper":40,
      "Sweet potato":25, "Pumpkin":35, "Drumstick":35, "Indian beans":30, "Sweet corn":30}
rice_and_grains = {"rice":60, "wheat":40, "barley":40, "quinoa":60, "oats":40, "corn":35, "millet":35}
dals = {"lentils":350 ,"chickpeas":230, "black beans":450, "kidney beans":340, "split peas":300,
        "mung beans":45, "black-eyed peas":60, "adzuki beans":45, "pinto beans":45, "navy beans":50, "soybeans":45}
dairy ={"ghee":250, "paneer":30, "curd":39, "lassi":40, "buttermilk":45}
cookware = {"pressure cooker":500, "tawa":250, "kadai":500, "idli steamer":700, "pressure pan":450,
            "handi":350, "appam pan":300, "dhokla stand":390, "puri press":340}
snack_sweet= {"samosa":35, "pakora":35, "bhajiya":40, "dhokla":20, "vada":20, "poha":30, "chaat":35,
              "samosa chaat":35, "jalebi":30, "gulab jamun":30, "barfi":50, "laddu":20, "halwa":40,  "kachori":33}
sec = [fruit, veg, rice_and_grains, dals, dairy, cookware, snack_sweet]
list_name = ["Fruits","Vegetables","Rice and grains","Dals","Dairy","Cookware","Snacks and sweets"]
c=0
items=[]

def menu(h):
    print("")
    for index,(key,value) in enumerate(h.items(),start=1):
        print(f"{index}.{key}:{value}".center(168," "))
def select(): #function to select itemss
    global items
    items =[]
    while True:
        l = []
        s=int(input("Enter the SECTION you want to buy from."))
        l.append(s)
        for x in range(len(list_name)):
            if s==x+1:
                print("Section:",list_name[x])
                menu(sec[x])
                while True:
                    print("Enter 0 when you are done selecting.")
                    n=int(input("Enter the ITEM number: "))
                    l.append(n)
                    if n == 0:
                        break
                    q=int(input("Enter the QUANTITY of item: "))
                    l.append(q)
                items.append(l)
        if s==0:
            print("Going back to Section selection.")
            break

def bill():
    global items
    for i in items:
        print(list(sec[i[0]].values())[i[1]] * i[2])




while True:
    b= int(input("Enter 0 to exit.\nEnter 1 to navigate grocery sections.\nEnter 2 to proceed to billing.\n"))

    if b==0:
        p=input("Are you done with billing (y/n)?: ")
        if p=='y':
            print("Collect your items at the counter.")
            print("Thanks for coming. Please visit again!")
            sys.exit()
        elif p=='n':
            print("Kindly checkout at billing first!")
        else:
            print("Invalid Choice")

    elif b==1:
        y= "Store sections".center(168,"=")
        print(y)
        for x in sec:
            c+=1
            print("\nSection: ",c,"-",list_name[c-1])
        select()
    elif b==2:
        bill()

    elif b!=0 or b!=1 or b!=2:
        print("Invalid Choice.Please Enter a Valid Option.")




'''
d="{:<5}"
e="{:>88}"
print("{},Kindly find your receipt below.".format(user))
print("_")
print(" bill you need to pay                Current bill = Rs.{}                       

print("_")
d="{:<5}"
e="{:>93}"
print(d.format(a), e.format(b))

print("                                                 {} {}".format(currbill,',',total))
f="{:.2f}".format(a)
g="{:.2f}".format(b)
print("Bill to be paid:                                 {}                                        {}".format(f,g))
h=total + billpay

binary="{:b}".format(50)
'''