rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock , paper, scissors]
user_choice = int(input("What would you like to choose ? Type 0 for rock , 1 for paper , 2 for scissors."))
print("Your choice: ")
print(game_images[user_choice])
print("Computer chose : ")

import random
random_system_choice = random.randint(0, 2)

if random_system_choice == 0:
    print(rock)
if random_system_choice == 1:
    print(paper)
if random_system_choice == 2:
    print(scissors)
print("RESULT!!!!")

#when the user chooses rock
if user_choice == 0 and random_system_choice == 0:
    print("It is a draw ,try again :/")
if user_choice == 0 and random_system_choice == 1:
    print("Computer chose paper , you lose :(")
if user_choice == 0 and random_system_choice == 2:
    print("Computer chose scissors , you win :)")

###When the user(you) choses paper###

if user_choice == 1 and random_system_choice == 0:
    print("Computer chose rock , you win :)")
if user_choice == 1 and random_system_choice == 1:
    print("It is a draw , try again :/")
if user_choice == 1 and random_system_choice == 2:
    print("Computer chose scissors , you lose :(")

#when the user chooses scissors
if user_choice == 2 and random_system_choice == 0:
    print("Computer chose rock , you lose :(")
if user_choice == 2 and random_system_choice == 1:
    print("Computer chose paper , you win :)")
if user_choice == 2 and random_system_choice == 2:
    print("It is a draw , try again :/")












