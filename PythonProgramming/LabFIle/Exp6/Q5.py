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
