try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Enter a valid number input !")
except ZeroDivisionError:
    print("Age can't be zero !")
