# 1.	Scan n values in range 0-3 and print the number of times each value has occurred.
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
count = [0,0,0]
if i in lst:
    if i == 0:
        count[0]+=1
    if i == 1:
        count[1]+=1
    if i == 1:
        count[2]+=1
print(f"Number of 1 = {count[0]},Number of 1 = {count[1]},Number of 2 = {count[2]}")
# 2. Create a tuple to store n numeric values and find average of all values
tp = 1,2,3,3,5,1
ave = sum(tp)/len(tp)
print("Average = ",ave)
# 3.	WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
lst.sort()
print("Runner up: ",lst[-2])
# 4. Create a dictionary of n persons where key is name and value is city. 
#   a) Display all names
#   b) Display all city names
#   c) Display student name and city of all students.
#   d) Count number of students in each city.

person_dict = {}
num_persons = int(input("Enter the number of persons: "))
for i in range(num_persons):
    name = input(f"Enter name for person {i + 1}: ")
    city = input(f"Enter city for {name}: ")
    person_dict[name] = city
print("All Names:")
for name in person_dict:
    print(name)
print("All Cities:")
unique_cities = set(person_dict.values())
for city in unique_cities:
    print(city)
print("Student Name and City:")
for name, city in person_dict.items():
    print(f"{name}: {city}")
city_counts = {}

for city in person_dict.values():
    city_counts[city] = city_counts.get(city, 0) + 1

print("Number of students in each city:")
for city, count in city_counts.items():
    print(f"{city}: {count}")
# 5.Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
#       a)	print all movie details
#       b)	display name of movies released before 2015
#       c)	print movies that made a profit.
#       d)	print movies directed by a particular director.

movies = {}
n = int(input("Enter the number of movies: "))
for i in range(n):
    name = input(f"Enter name of movie {i + 1}: ")
    year = int(input(f"Enter release year for {name}: "))
    director = input(f"Enter director name for {name}: ")
    production_cost = float(input(f"Enter production cost for {name}: "))
    collection = float(input(f"Enter collection made (earning) for {name}: "))
    movies[name] = {
        "Year": year,
        "Director": director,
        "Production Cost": production_cost,
        "Collection": collection
    }
print("\nAll Movie Details:")
for movie, details in movies.items():
    print(f"{movie}: {details}")
print("\nMovies Released Before 2015:")
for movie, details in movies.items():
    if details["Year"] < 2015:
        print(movie)
print("\nMovies That Made a Profit:")
for movie, details in movies.items():
    if details["Collection"] > details["Production Cost"]:
        print(movie)
director_name = input("\nEnter director name to filter movies: ")
print(f"\nMovies Directed by {director_name}:")
for movie, details in movies.items():
    if details["Director"].lower() == director_name.lower():
        print(movie)
