import random

def roll():
  min_value = 1
  max_value = 6

  roll = random.randint(min_value, max_value)

  return roll

value = roll()

while True:
  players = input("Enter the number of players (2-4): ")

  if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Must be between 2 - 4 players.")
  else:
    print("Invalid, try again.")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

  for player_index in range(players):
    print(f"\n*****Player number {player_index + 1} trun has just started!*****")
    print(f"Your total score is: {players_scores[player_index]}. \n")
    current_score = 0

    while True:
      want_to_roll = input("Would you like to roll (y)? ").lower()
      if want_to_roll != "y":
        break

      value = roll()
      if value == 1:
        print("You rolled a 1! Trun done!")
        current_score = 0
        break
      else:
        current_score += value
        print(f"You rolled a: {value}")

      print(f"Your score is: {current_score}")

    players_scores[player_index] += current_score
    print(f"Your total score is: {players_scores[player_index]}")

max_score = max(players_scores)
winning_index = players_scores.index(max_score)
print(f"Player number {winning_index + 1} is the winner with score of: {max_score}")