# 3.	Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM)):
#       a.	Display details of all cities
#       b.	Display city names with population more than 10Lakhs
#       c.	Display sum of areas of all cities

citiesPopGT10Lakhs = []
totalArea = 0

with open("cities.txt", "r") as f: 
    x = f.read()
    for i in x.split("\n"):
        if i:
            cl = i.split()
            print(f"""City Name: {cl[0]}
    Population: {cl[1]}
    Area: {cl[2]} sq KM""")
            totalArea += float(cl[2])
            if float(cl[1])>10:
                citiesPopGT10Lakhs.append(cl[0])
print("Cities with more than 10 Lakh people: ")
for i in citiesPopGT10Lakhs:
    print(i,end=" ")

print(f'\nTotal City area: {totalArea}')
