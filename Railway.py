import numpy as np

class RailwaySystem:
    def __init__(self):
        self.users = {}
        self.trains = {
            'Train1': {'name': 'Dehradun Shatabdi', 'seats': np.array([100]), 'route': np.array(['Delhi', 'Haridwar', 'Dehradun'])},
            'Train2': {'name': 'Nanda Devi', 'seats': np.array([80]), 'route': np.array(['Dehradun', 'Haridwar', 'Rishikesh'])},
            'Train3': {'name': 'Mussoorie Express', 'seats': np.array([90]), 'route': np.array(['Dehradun', 'Mussoorie'])},
            'Train4': {'name': 'Dehradun Amritsar Express', 'seats': np.array([85]), 'route': np.array(['Dehradun', 'Chandigarh', 'Amritsar'])}
        }

    def create_account(self, username, password):
        if username in self.users:
            return "Account already exists."
        else:
            self.users[username] = {'password': password, 'tickets': []}
            return "Account created successfully."

    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return "Login successful."
        else:
            return "Invalid username or password."

    def book_ticket(self, username, train_id):
        if username not in self.users:
            return "Please login first."
        if train_id not in self.trains:
            return "Train not found."
        if self.trains[train_id]['seats'][0] > 0:
            self.trains[train_id]['seats'][0] -= 1
            self.users[username]['tickets'].append(train_id)
            return "Ticket booked successfully."
        else:
            return "No seats available."

    def get_route(self, train_id):
        if train_id in self.trains:
            route = self.trains[train_id]['route']
            return " -> ".join(route)
        else:
            return "Train not found."

rs = RailwaySystem()
logged_in_user = None
print("Welcome to Railway System")
while True:
    print("1. Create Account")
    print("2. Login")
    print("3. Book Ticket")
    print("4. View Train Route")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        print(rs.create_account(username, password))

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        response = rs.login(username, password)
        print(response)
        if response == "Login successful.":
            logged_in_user = username

    elif choice == '3':
        if logged_in_user:
            print("Available Trains:")
            for train_id, train_info in rs.trains.items():
                print(f"{train_id}: {train_info['name']} - Seats Left: {train_info['seats'][0]}")
            train_id = input("Enter train ID to book: ")
            print(rs.book_ticket(logged_in_user, train_id))
        else:
            print("Please login first.")

    elif choice == '4':
        if logged_in_user:
            for train_id, train_info in rs.trains.items():
                route = rs.get_route(train_id)
                print(f"{train_id} ({train_info['name']}): {route}")
        else:
            print("Please login first.")

    elif choice == '5':
        print("Thank you for using Railway System. Goodbye!")
        break
