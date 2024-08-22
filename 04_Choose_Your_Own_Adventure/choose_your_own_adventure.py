name = input("Type your name: ")
print(f"Welcome, {name} to this adventure!!!")

answer = input("You are ona dirt road, it has come to an end and you can go left or right. Which way you would like to go? ").lower()

if answer == "left":
  answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

  if answer == "swim":
    print("You swam across and were eaten by an alligator.")
  elif answer == "walk":
    print("You walked for many miles, ran out of water and you lost the game.")
  else:
    print("Not a valid option, You lose!!!")
elif answer == "right":
  answer = input("You come to a bridge, it looks wobbly, do you want yo cross it or head back (cross/back)? ").lower()

  if answer == "back":
    print("You go back and lose.")
  elif answer == "cross":
    answer = input("You cross the bridge and meet a stranger. Do you want to talk with them (Yes/No) ? ").lower()

    if answer == "yes":
      print("You talked to the stranger and he gave you a gold and You win!!!")
    elif answer == "no":
      print("You ignore the stranger and he is offended and you lose!!!")
    else: 
      print("Not a valid option, You lose!!!")
  else:
    print("Not a valid option, You lose!!!")
else:
  print("Not a valid option, You lose!!!")

print(f"Thanks for trying {name}!!!")