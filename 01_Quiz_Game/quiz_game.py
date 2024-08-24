import random
import time
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load sound effects
timer_sound = pygame.mixer.Sound("timer.mp3")
correct_sound = pygame.mixer.Sound("right_answer.mp3")
wrong_sound = pygame.mixer.Sound("wrong_answer.mp3")
time_up_sound = pygame.mixer.Sound("time_up.mp3")

# Define a list of questions with corresponding correct answers
questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Computer Personal Unit", "C) Central Processor Unit", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does GPU stand for?",
        "options": ["A) Graphics Processing Unit", "B) Gaming Processing Unit", "C) Graphical Performance Unit", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A) Random Access Memory", "B) Read Access Memory", "C) Run Access Memory", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does PSU stand for?",
        "options": ["A) Power Supply Unit", "B) Personal System Unit", "C) Portable Storage Unit", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A) HyperText Markup Language", "B) HighText Markup Language", "C) HyperTool Multi Language", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["A) Hypertext Transfer Protocol", "B) Hypertext Transmission Protocol", "C) Hightext Transfer Protocol", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does USB stand for?",
        "options": ["A) Universal Serial Bus", "B) Universal System Bus", "C) Unique Serial Bus", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does SSD stand for?",
        "options": ["A) Solid State Drive", "B) System Storage Device", "C) Super Speed Drive", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does BIOS stand for?",
        "options": ["A) Basic Input Output System", "B) Binary Input Output System", "C) Basic Integrated Operating System", "D) None of the above"],
        "answer": "a"
    },
    {
        "question": "What does LAN stand for?",
        "options": ["A) Local Area Network", "B) Large Area Network", "C) Long Area Network", "D) None of the above"],
        "answer": "a"
    }
]

# Function to ask a multiple-choice question with a time limit
def ask_question(question, options, correct_answer, time_limit=5):
    print(question)
    for option in options:
        print(option)
    
    # Start timer sound
    timer_sound.play(-1)  # Loop indefinitely until stopped

    start_time = time.time()
    answer = input("Your answer (A/B/C/D): ").lower()

    # Check if the time limit has been exceeded
    if time.time() - start_time > time_limit:
        timer_sound.stop()
        time_up_sound.play()  # Play time's up sound
        time.sleep(time_up_sound.get_length())  # Wait for the time's up sound to finish
        print("Time's up!")
        return False
    
    # Stop timer sound
    timer_sound.stop()

    # Check if the time limit has been exceeded
    if time.time() - start_time > time_limit:
        print("Time's up!")
        return False
    
    if answer == correct_answer:
        correct_sound.play()
        time.sleep(correct_sound.get_length())  # Wait for the correct sound to finish playing
    else:
        wrong_sound.play()
        time.sleep(wrong_sound.get_length())  # Wait for the wrong sound to finish playing
    
    return answer == correct_answer

# Function to display feedback based on the score
def display_feedback(score, max_score):
    if score == max_score:
        print("Excellent! You got all questions correct!")
    elif score >= max_score * 0.75:
        print("Great job! You got most of them correct.")
    elif score >= max_score * 0.5:
        print("Good effort! You got half of the questions right.")
    else:
        print("Keep practicing! You'll get better.")

# Main game function
def play_quiz():
    print("Welcome to my computer quiz!!!")
    
    playing = input("Do you want to play? ").lower()
    if playing != "yes":
        quit()

    print("Okay! Let's play...")
    score = 0

    # Shuffle the list of questions to randomize the order
    random.shuffle(questions)
    
    # Ask each question
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    # Display the final score
    display_feedback(score, len(questions))

# Start the quiz game
play_quiz()