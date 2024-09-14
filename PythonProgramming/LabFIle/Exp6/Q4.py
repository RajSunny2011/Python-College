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
