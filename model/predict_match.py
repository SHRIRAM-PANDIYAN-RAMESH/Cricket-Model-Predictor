import pandas as pd
import joblib

# Load trained model
model = joblib.load(r"C:\Users\rames\Desktop\WARPE_Programs\Web_Scraping_Automation_Project_2\model\ipl_predictor.pkl")

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\rames\Desktop\WARPE_Programs\Web_Scraping_Automation_Project_2\data\processed\clean_matches.csv")

# Calculate team win rates
teams = set(df["team1"]).union(set(df["team2"]))

team_win_rates = {}

for team in teams:

    matches_played = (
        (df["team1"] == team) |
        (df["team2"] == team)
    ).sum()

    matches_won = (
        df["winner"] == team
    ).sum()

    team_win_rates[team] = matches_won / matches_played


print("\nAVAILABLE TEAMS")
print("-" * 50)

for team in sorted(team_win_rates.keys()):
    print(team)

print("\n")

# User input
team1 = input("Enter Team 1: ")
team2 = input("Enter Team 2: ")
toss_winner = input("Enter Toss Winner: ")

# Validation
if team1 not in team_win_rates:
    print(f"\nError: {team1} not found!")
    exit()

if team2 not in team_win_rates:
    print(f"\nError: {team2} not found!")
    exit()

# Feature creation
team1_win_rate = team_win_rates[team1]
team2_win_rate = team_win_rates[team2]

toss_advantage = int(toss_winner == team1)

features = pd.DataFrame([
    {
        "team1_win_rate": team1_win_rate,
        "team2_win_rate": team2_win_rate,
        "toss_advantage": toss_advantage
    }
])

# Prediction
prediction = model.predict(features)[0]

# Probabilities
probabilities = model.predict_proba(features)[0]

team1_probability = probabilities[1] * 100
team2_probability = probabilities[0] * 100

print("\nMATCH ANALYSIS")
print("-" * 50)

print(f"Team 1: {team1}")
print(f"Team 2: {team2}")

print(f"\n{team1} Win Rate: {team1_win_rate:.3f}")
print(f"{team2} Win Rate: {team2_win_rate:.3f}")

print(f"\nToss Winner: {toss_winner}")

print("\nWIN PROBABILITY")
print("-" * 50)

print(f"{team1}: {team1_probability:.2f}%")
print(f"{team2}: {team2_probability:.2f}%")

if prediction == 1:
    winner = team1
else:
    winner = team2

print("\nPREDICTED WINNER")
print("-" * 50)

print(winner)
