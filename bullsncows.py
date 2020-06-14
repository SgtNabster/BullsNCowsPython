import random
# Declare variables
number = []
attempts = 0
# defines a function that creates a random 4 digit number (all unique digits)
def make_number():
    while len(number) < 4:
        x = random.randrange(0,9)
        if x not in number:
            number.append(x)

def play_game():
    # Accesses attempts
    global attempts
    # Increments attempts
    attempts +=1
    # sets bulls and cows
    cows = 0
    bulls = 0
    # asks user for there guess
    choice = input("Please enter a 4 digit number:    ")
    #creates a place to store guess
    guess = []
    # 
    for i in range (4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if guess[i] == number[j]:
                cows += 1
    for x in range (4):
        if guess[x] == number[x]:
            bulls += 1
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    if bulls == 4:
        print("Youve won after: {} attempts!".format(attempts))
    elif bulls != 4:
        play_game()

make_number()
play_game()