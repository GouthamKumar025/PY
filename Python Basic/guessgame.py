#Building a number guessing game
i=1
guess=9
while i<=3:
    ans=int(input("Enter the number: "))
    if ans==guess:
        print("You Won!")
        break
    i=i+1
else:
    print("You Failed")
