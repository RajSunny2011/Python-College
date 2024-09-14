class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.goals_scored = 0
        self.assists = 0
        self.yellow_cards = 0
        self.red_cards = 0

    def score_goal(self):
        self.goals_scored += 1

    def assist(self):
        self.assists += 1

    def receive_yellow_card(self):
        self.yellow_cards += 1

    def receive_red_card(self):
        self.red_cards += 1

    def print_stats(self):
        print(f"Player: {self.name} (#{self.number})")
        print(f"Goals Scored: {self.goals_scored}")
        print(f"Assists: {self.assists}")
        print(f"Yellow Cards: {self.yellow_cards}")
        print(f"Red Cards: {self.red_cards}")

class Team:
    def __init__(self):
        self.players = {}

    def add_player(self, name, number):
        self.players[number] = Player(name, number)

    def get_player_by_number(self, number):
        return self.players.get(number)

team = Team()
for i in range(4):
    player_name = input("Enter player name: ")
    player_number = input(f"Enter number for {player_name}: ")
    team.add_player(player_name, player_number)

while True:
    choice = input("Enter:\n\t1) Add Goal\n\t2) Add assist\n\t3) Give yellow card\n\t4) Give red card\n\t5) Print Stats\n\t0) To stop\nEnter: ")
    if choice == '0':
        break
    player_number = input("Enter player number: ")
    player = team.get_player_by_number(player_number)
    if player:
        if choice == '1':
            player.score_goal()
        elif choice == '2':
            player.assist()
        elif choice == '3':
            player.receive_yellow_card()
        elif choice == '4':
            player.receive_red_card()
        elif choice == '5':
            player.print_stats()
    else:
        print(f"No player found with number: {player_number}")
