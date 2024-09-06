# Python Projects

This repository contains multiple Python projects. Each project demonstrates different programming concepts and provides an engaging user experience.

---

## Project 1: Quiz Game

### Description
The Quiz Game is an interactive and engaging project where users answer multiple-choice questions within a given time limit. To make the experience more exciting, background music plays throughout the game, and different sound effects are triggered for correct and wrong answers. At the end of the quiz, users receive feedback based on their score.

### Features
- **Multiple-Choice Questions:** A set of questions is provided, and the user must choose the correct answer.
- **Time Limit:** Each question must be answered within a specified time.
- **Background Music:** Continuous music plays during the quiz to create a fun atmosphere.
- **Sound Effects:** Different sounds for correct and wrong answers add to the excitement.
- **Feedback System:** Based on the final score, feedback is given to the user.

### Technology Used
- **Python**
- **Pygame** (for handling music and sound effects)

### How to Run
1. Ensure Python is installed on your machine.
2. Install the `pygame` module using `pip install pygame`.
3. Run the script using `python quiz_game.py`.

---

## Project 2: Number Guessing Game

### Description
The Number Guessing Game challenges the user to guess a number within a specified range and a limited number of guesses. The user selects the number of rounds, the difficulty level, and the upper range of the number to guess. Points are awarded for correct guesses, and points are deducted for incorrect guesses.

### Features
- **Customizable Rounds:** The user chooses how many numbers they want to guess.
- **Difficulty Levels:** Three difficulty levels (Easy, Medium, Hard) determine the number of guesses allowed.
- **Points System:** 10 points for a correct guess, and 2 points are deducted for each incorrect guess.
- **Score Display:** The total score is displayed at the end of the game.

### Technology Used
- **Python**

### How to Run
1. Ensure Python is installed on your machine.
2. Run the script using `python number_guessing_game.py`.

---

## Project 3: Rock-Paper-Scissors

### Description
The Rock-Paper-Scissors game allows the user to play against the computer in a classic game of strategy. The user selects either rock, paper, or scissors, and the computer randomly chooses its move. The winner is displayed for each round, and the user can quit the game at any time to see the final winner.

### Features
- **User vs. Computer:** Play against the computer with random selections.
- **Round-Based:** The winner is determined for each round.
- **Final Winner:** The final winner is displayed when the user quits the game.

### Technology Used
- **Python**

### How to Run
1. Ensure Python is installed on your machine.
2. Run the script using `python rock_paper_scissors.py`.

## Project 4: Select Your Own Adventure

### Description
The Select Your Own Adventure game is an interactive text-based adventure where the user makes choices that determine the outcome of the story. Players navigate through different scenarios by choosing directions and actions, leading to various endings. The game provides an engaging way to explore decision-making and storytelling.

### Features
- **Interactive Choices:** Users choose their path at each decision point.
- **Multiple Outcomes:** Different scenarios based on the user's choices, leading to different endings.
- **Text-Based:** A narrative-driven game where all interactions are text-based.

### Technology Used
- **Python**

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script using `select_your_own_adventure.py`.
3. Run the script using `python select_your_own_adventure.py`.

## Project 5: Password Manager

### Description
The Password Manager is a secure application that allows users to store, retrieve, and manage their passwords in an encrypted format. It uses the `cryptography` library to encrypt passwords, ensuring that stored credentials are safe from unauthorized access. The application supports the addition of new passwords and viewing existing ones, with strong password validation and a master password for enhanced security.

### Features
- **Password Encryption:** Passwords are stored securely using the `cryptography` library, ensuring they are safe from unauthorized access.
- **Master Password:** A master password is required to unlock the stored passwords, adding an extra layer of security.
- **Password Strength Validation:** Ensures that passwords meet certain criteria (length, inclusion of upper/lower case letters, numbers, and special characters) before they are stored.
- **Masked Password Display:** When viewing passwords, they are masked by default, with an option to reveal the full password.
- **Auto-Key Generation:** Automatically generates an encryption key if one does not exist.

### Technology Used
- **Python**
- **Cryptography** (for encryption and decryption of passwords)
- **Hashlib** (for secure hashing of the master password)

### How to Run
1. Ensure Python is installed on your machine.
2. Install the `cryptography` module using `pip install cryptography`.
3. Run the script using `python password_manager.py`.
4. Follow the prompts to add new passwords, view existing ones, or quit the application.

### Security Note
- **Key Storage:** The encryption key is stored in a file called `key.key`. Keep this file secure as it is required to decrypt your passwords.
- **Master Password:** Choose a strong master password as it is used to generate the key for encrypting and decrypting your stored passwords.

## Project 6: Dice Game

### Description
This is simple dice game where players take turns rolling a die to accumulate points. Each player can choose to either roll the die to add to their turn's score or hold to add the turn's score to their total. Rolling a 1 ends the turn and loses all points accumulated during that turn. The game continues until a player reaches a maximum score of 50, at which point the player with the highest score is declared the winner.

### Features
- **Turn-Based Play:** Players take turns rolling a die to accumulate points for each turn.
- **Risk and Reward:** Players can choose to roll again to increase their turn score but risk losing all points if they roll a 1.
- **Flexible Player Count:** Supports 2 to 4 players.
- **Winning Condition:** The game ends when a player reaches a score of 50 or more, and the player with the highest score wins.

### Technology Used
- **Python**
- **Random** (for simulating dice rolls)

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script as `dice_game.py`.
3. Run the script using `python dice_game.py`.
4. Follow the prompts to enter the number of players, and then take turns rolling the dice.

## Project 7: Mad Libs Generator

### Description
The Mad Libs Generator is a fun and interactive project that allows users to create a customized story by filling in blanks with their own words. The script reads a story from a text file, identifies placeholders for words enclosed in angle brackets, and prompts the user to provide words to replace these placeholders. Once all placeholders are filled, the script generates a complete, personalized story.

### Features
- **Story Input:** Reads a story from a text file with placeholders enclosed in angle brackets.
- **User Interaction:** Prompts the user to input words for each placeholder.
- **Story Generation:** Replaces placeholders with user-provided words to create a customized story.

### Technology Used
- **Python**

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script as `madlibs_generator.py`.
3. Create a text file named `story.txt` with the story, using angle brackets (< and >) for placeholders.
4. Run the script using `python madlibs_generator.py`.
5. Follow the prompts to enter words for each placeholder, and the script will generate the customized story.

## Project 8: Slot Machine

### Description
The Slot Machine project simulates a classic slot machine experience where players can deposit money, place bets, and spin the slots. Players can choose the number of lines to bet on and the amount to bet per line. The slot machine consists of different symbols with associated values, and the game calculates winnings based on the symbols that align across the lines. The player's balance is updated based on their bets and winnings.

### Features
- **Deposit Functionality:** Allows players to deposit money into their balance.
- **Betting System:** Players can choose the number of lines to bet on and the amount to bet per line.
- **Slot Machine Spin:** Randomly generates slot machine outcomes with various symbols.
- **Winning Calculation:** Checks for winning lines and calculates winnings based on symbol values.
- **Balance Management:** Updates the player's balance based on bets and winnings.


### Technology Used
- **Python**
- **Random** (for simulating slot machine spins)

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script as `slot_machine.py`.
3. Run the script using `python slot_machine.py`.
4. Follow the prompts to deposit money, select the number of lines and bet amount, and spin the slot machine.

## Project 9: Turtle Racing

### Description
The Turtle Racing project is an interactive game where players can specify the number of turtles to race across the screen. Each turtle is given a unique color, and they race from the bottom to the top of the screen. The race continues until one turtle crosses the finish line, and the color of the winning turtle is displayed.

### Features
- **Customizable Racers:** Players can choose the number of turtles (racers) from 2 to 10.
- **Colorful Turtles:** Each turtle is assigned a unique color for easy identification.
- **Race Animation:** The turtles race across the screen with random movements until one reaches the finish line.
- **Winner Announcement:** The color of the winning turtle is displayed after the race concludes.

### Technology Used
- **Python**
- **Turtle Module** (for creating and animating the turtles)

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script as `turtle_racing.py`.
3. Run the script using `python turtle_racing.py`.
4. Follow the prompts to enter the number of turtles, and watch the turtles race across the screen.


## Project 10: WPM Typing Test

### Description
The WPM Typing Test project is a command-line application designed to measure typing speed. The test displays a random passage of text, and the user types it as quickly and accurately as possible. The program calculates and displays the user's Words Per Minute (WPM) as they type. It provides visual feedback on correct and incorrect characters and allows the user to correct mistakes during the test.

### Features
- **Typing Speed Measurement:** Calculates and displays the user's typing speed in Words Per Minute (WPM).
- **Text Display:** Shows a random passage of text for the user to type.
- **Real-Time Feedback:** Highlights correct characters in green and incorrect characters in red.
- **Error Correction:** Allows the user to correct mistakes by using the backspace key.
- **Escape Key:** Provides an option to exit the test by pressing the Escape key.

### Technology Used
- **Python**
- **Curses Module** (for handling terminal input and output)

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script as `wpm_typing_test.py`.
3. Create a text file named `wpm_typing_texts.txt` with sample passages, each on a new line.
4. Run the script using `python wpm_typing_test.py`.
5. Follow the on-screen instructions to start the test, type the displayed text, and see your typing speed.

## Project 11: Shortest Path Finder

### Description
The Shortest Path Finder project is an interactive command-line application that visualizes the process of finding the shortest path in a maze. The user can choose between two algorithms: Breadth-First Search (BFS) and A* (A-star), allowing them to compare and analyze their performance. The maze contains walls, a start point, and an endpoint. The program displays the search process in real-time and highlights the final shortest path once found.

### Features
- **Algorithm Selection:** Users can switch between BFS and A* algorithms and compare their efficiency.
- **Real-Time Visualization:** Displays the search process dynamically as the algorithm explores the maze.
- **Path Highlighting:** Shows the shortest path once the algorithm reaches the endpoint.
- **Interactive User Input:** Users can select which algorithm to use at runtime.
- **Maze Customization:** Users can modify the maze structure and dimensions to test various scenarios.
- **Performance Comparison:** Analyze the performance of BFS and A* in terms of speed and path length.

### Technology Used
- **Python**
- **Curses Module** (for handling terminal input and output)
- **Queue And Heaps** (for BFS and A* algorithms) 

### How to Run
1. Ensure Python is installed on your machine.
2. Save the script as `shortest_path_finder.py`.
3. Run the script using `python shortest_path_finder.py`.
4. Follow the on-screen instructions to select between BFS and A* algorithms.
5. Watch as the algorithm explores the maze, and compare the final paths for both algorithms.

