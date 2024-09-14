import pandas as pd
import matplotlib.pyplot as plt

filepath=r"matches.csv"
df=pd.read_csv(filepath)
print(f"discription: {df.describe()}")

print(f"1st 10 data: {df.head(10)}")

print(f"last 10 data: {df.tail(10)}")

print(f"Total Number of Matches played: {df.shape[0]}")

print(f"Number of seasons: {df['season'].nunique()}")

print(f"Number of cities match held: {df['city'].nunique()}")

print(f"Team with the most wins: {df['winner'].value_counts().idxmax()}")

toss_winner_matches = sum(df['toss_winner'] == df['winner'])
print("Number of matches won by the team that won the toss: ",toss_winner_matches)

super_over_matches = df[df['super_over'] == 'Y'].shape[0]
print("Number of matches that went to a super over: ",super_over_matches)

print(f"Number of match per season: {df['season'].value_counts()}")
print(f"Number of matches per city: {df['city'].value_counts()}")

teams = pd.concat([df['team1'], df['team2']])
losses = teams.value_counts() - df['winner'].value_counts()
team_most_losses = losses.idxmax()

print("Team with most losses: ", team_most_losses)

print(f"Player with the most wickets: {df[df['result'] == 'wickets']['player_of_match'].value_counts().idxmax()}")


# graphs:- 




top_10_players = df['player_of_match'].value_counts().head(10)
top_10_players.plot(kind='barh', color='r')
plt.title('Top 10 Players with Most Player of the Match Awards')
plt.xlabel('Number of Awards')
plt.ylabel('Player')
plt.show()



top_10_cities = df['city'].value_counts().head(10)
top_10_cities.plot(kind='bar', color='green')
plt.title('Top 10 Cities by Number of Matches')
plt.xlabel('City')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


matches_over_years = df.groupby('season')['id'].count()
matches_over_years.plot(kind='bar', color='skyblue')
plt.title('Number of Matches Over the Years')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()