# Exercise 1
a = input()
b = int(a[0])
c = int(a[1])
result = b + c
print(result)

# b = str(a)
# c = str(int(b[0])+int(b[1]))
# print("The addition of "+b[0]+" and "+ b[1]+" is " + c)

# Exercise 2 - bmi calculator

height = input("Enter your height(in m): ")
weight = input("Enter your weight(in kg): ")
bmi = int(weight) / float(height) ** 2
print(int(bmi))

# Final Project - tip calculator

print("Welcome to Tip Calculator")
bill = float(input("What was the total bill:$"))
percentage = int(input("What percentage would you like to give? 10, 12, 15? "))
split = int(input("How many person to split the bill? "))
tip = bill * (percentage/100)
tip_amount = bill + tip
split_amount = tip_amount / split
print(f"Each person should pay ${round(split_amount,2)}")
