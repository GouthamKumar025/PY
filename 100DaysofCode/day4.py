'''# Exercise - 1
import random
random_decimal = random.random()
print(random_decimal*5)

# Exercise - 2
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_number = random.randint(0,1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")


# Exercise - 3
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameasCSV = input("Give me everybody's name: ")
names = nameasCSV.split(",")
print(names)
length = len(names)
a = random.randint(0,length-1)
print(names[a])


# Exercise - 4
#  Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 👆
columns = int(position[0]) - 1
rows = int(position[1]) - 1
map[rows][columns] = "X"
#  Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
'''

# Final Project - Rock Paper Scissor

import random
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
game_options = [rock,paper,scissors]
print("Hey ! Welcome to Rock Stone Paper Scissors Game\n Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors ")
user = int(input())
if 3 <= user < 0:
    print("Invalid Input.. Try some other values")
else:
    print(game_options[user])
computer = random.randint(0,2)
print("Computer Chose: ")
print(game_options[computer])
if user == 1 and computer == 0:
    print("You Won !")
elif user == 0 and computer == 1:
    print("You Lose !")
elif user == 2 and computer == 1:
    print("You Won !")
elif user == 1 and computer == 2:
    print("You Lose !")
elif user == 0 and computer == 2:
    print("You Won !")
elif user == 2 and computer == 0:
    print("You Lose !")
else:
    print("Match Draw")






