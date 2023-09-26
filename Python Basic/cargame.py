# Building a car game
info = input("Type Help for knowing the info of the game: ")
if info.lower() == "help":
    print('''start - to start the car
stop  - to stop the car
quit  - for quiting the game
          ''')
    cmd = " "
    started = False
    stopped = False
    while True:
        cmd = input("Enter your command here: ").lower()
        if cmd == "start":
            if started:
                print("The car is already been started")
            else:
                started = True
                print("The car is started")
        elif cmd == "stop":
            if stopped:
                print("The car is already been stopped")
            else:
                stopped = True
                print("The car is stopped")
        elif cmd == "quit":
            break
        else:
            print("Sorry, I can't understand")