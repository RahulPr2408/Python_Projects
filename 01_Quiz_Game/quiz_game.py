print("Welcome to my computer quiz!!!")

plyaing = input("Do you want to play? ").lower()

if plyaing != "yes":
  quit()

print("Okay! Let's play...")
score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")


print(f"You got {score} questions correct!!!")