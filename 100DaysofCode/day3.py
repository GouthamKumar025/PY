# Exercise - 1
# Even or Odd
value = int(input("Enter the number: "))
if value % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Exercise - 2
# BMI Calculator
print("Welcome to the BMI Calculator")
height = float(input("Enter your height(in m): "))
weight = float(input("Enter your weight(in kg): "))
bmi = weight / height**2
if bmi < 18.5:
    bmi_status = "Under weight"
elif 18.5 <= bmi < 25:
    bmi_status = "Normal weight"
elif 25 <= bmi < 30:
    bmi_status = "Over weight"
elif 30 <= bmi < 35:
    bmi_status = "Obese"
else:
    bmi_status = "Clinically Obese"
print(f"Your BMI is {round(bmi,2)} and {bmi_status}")

# Exercise - 3
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is leap year")
else:
    print("The year is not leap year")

# Pizza ordering platform
print("Welcome to Pizza Ordering Platform")
size = input("Which size pizza do you want? S? M? L? ")
add_pepperoni = input("Do you want add pepperoni ? Y or N ")
extra_cheese = input("Do you want to add extra cheese ? Y or N ")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
if size == 'S':
    if add_pepperoni == 'Y':
        amount = 15 + 2
    elif add_pepperoni == 'Y' and extra_cheese == 'Y':
        amount = 15 + 2 + 1
    else:
        amount = 15 + 1
    print(f"Your final bill order is ${amount}")
elif size == 'M':
    if add_pepperoni == 'Y':
        amount = 20 + 3
    elif add_pepperoni == 'Y' and extra_cheese == 'Y':
        amount = 20 + 3 + 1
    else:
        amount = 20 + 1
    print(f"Your final bill order is ${amount}")
else:
    if add_pepperoni == 'Y':
        amount = 25 + 3
    elif add_pepperoni == 'Y' and extra_cheese == 'Y':
        amount = 25 + 3 + 1
    else:
        amount = 25 + 1
    print(f"Your final bill order is ${amount}")


# Love Calculator

name1 = input("Enter your name: ").lower()
name2 = input("Enter your love name: ").lower()
combined = name1 + name2
t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e = combined.count('e')
l = combined.count('l')
o = combined.count('o')
v = combined.count('v')
e = combined.count('e')
count1 = str(t + r + u + e)
count2 = str(l + o + v + e)
percentage = int(count1 + count2)
if percentage <=10 and percentage >= 90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")
elif 40 <= percentage <= 50:
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")

# Final Project
print("Welcome to Treasure island\n Your mission is to find the treasure")
move = input("You are in a cross junction whether you want to move right or left? ")
if move == "left":
    opinion = input("You are near a lake. Whether you want to swim or wait? ")
    if opinion == "wait":
        door = input("There are three doors of yellow, red, blue. Which door you want to enter? ")
        if door == "yellow":
            print("Hey! Congratulations you have found out the treasure")
        else:
            print("You are caught up with beast.... Game Over !!!")
    else:
        print("Game Over !!!")
else:
    print("Game Over !!!")






