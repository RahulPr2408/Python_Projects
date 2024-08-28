import random

# Ask the user for the number of rounds they want to play
while True:
    num_rounds = input("How many numbers would you like to play? ")

    if num_rounds.isdigit() and int(num_rounds) > 0:
        num_rounds = int(num_rounds)
        break
    else:
        print("Please enter a valid positive number.")

# Ask the user for the difficulty level
while True:
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()

    if difficulty in ['easy', 'medium', 'hard']:
        break
    else:
        print("Please choose a valid difficulty level.")

# Set the number of guesses based on difficulty
if difficulty == 'easy':
    max_guesses = 5
elif difficulty == 'medium':
    max_guesses = 3
else:
    max_guesses = 2

total_score = 0

for round in range(1, num_rounds + 1):
    print(f"\nRound {round}/{num_rounds}")

    # Ask the user for the top of range
    while True:
        top_of_range = input("Type a number for the upper range: ")

        if top_of_range.isdigit() and int(top_of_range) > 0:
            top_of_range = int(top_of_range)
            break
        else:
            print("Please type a valid number greater than 0.")

    random_number = random.randint(0, top_of_range)
    guesses = 0
    round_score = 0

    while guesses < max_guesses:
        guesses += 1
        user_guess = input(f"Guess {guesses}/{max_guesses}: ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number.")
            continue

        if user_guess == random_number:
            print("You got it!!!")
            round_score = 10 - (guesses - 1) * 2  # 10 points minus 2 points per wrong guess
            total_score += round_score
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    if round_score == 0:
        print(f"Out of guesses! The correct number was {random_number}.")
    
    print(f"Score for this round: {round_score} points")

print(f"\nGame over! Your total score is {total_score} points.")
