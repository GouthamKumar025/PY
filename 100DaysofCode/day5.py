# Exercise 1 - calculating average

students = input("Enter the students height: ").split()
for n in range(0,len(students)):
    students[n] = int(students[n])
print(students)
# calculating averages
sum = 0
for i in range(0,len(students)):
    sum += students[i]
print(round(sum/len(students)))

#Calculating maximum marks
students = input("Enter the students marks: ").split()
for n in range(0,len(students)):
    students[n] = int(students[n])
print(students)

max = 0
for i in range(0,len(students)):
    if students[i] > max:
        max = students[i]
    else:
        break
print(f"The maximum number in the list is {max}")

#calculating the sum of even numbers

total_sum = 0
for i in range(0,101,2):
    total_sum += i
print(total_sum)


# Fizz Buzz game

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#Final Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for char in range(1,nr_letters+1):
    password += random.choice(letters)
for char in range(1,nr_symbols+1):
    password += random.choice(symbols)
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)

print(password)