import time
import random

def menu():
    print("Welcome to my Rock Paper Scissor Game made in python")
    time.sleep(2)
    choice = input("What are you choosing? Rock(R) Paper(P) or Scissors(s)")
    result(choice)

def result(choice):
    choice = choice.lower()
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "r"
    elif computer == 2:
        computer = "p"
    elif computer == 3:
        computer = "s"

    if choice == computer:
        draw(computer)
    elif choice == 'r':
        if computer == 'p':
            computer = 'Paper'
            choice = 'rock'
            playerlost(choice, computer)
        elif computer == 's':
            computer = 'scissor'
            choice = 'Rock'
            playerwon(choice, computer)
    elif choice == 'p':
        if computer == 's':
            computer = "Scissor"
            choice = 'paper'
            playerlost(choice, computer)
        elif computer == 'r':
            computer = "rock"
            choice = 'Paper'
            playerwon(choice, computer)
    elif choice == 's':
        if computer == 'r':
            computer = "Rock"
            choice = 'scissor'
            playerlost(choice, computer)
        elif computer == 'p':
            computer = "paper"
            choice = 'Scissor'
            playerwon(choice, computer)
    else:
        error = input("an unexpected error occurred, Do you want to try again? (Yes/No")
        error = error.lower()
        if error == 'yes':
            menu()
        else:
            print("Exitting out in 2 Seconds")
            time.sleep(2)
            exit
    

def playerwon(choice, computer):
    messages = ['Only losers lose', 'Welcome to the cool kids club', 'you could beat him blindfolded', 'Winning is only for cool people']
    msg = random.choice(messages)
    print(choice + " beats " + computer + " So you win :D " + msg)

def playerlost(choice, computer):
    messages = ['Defeated!', 'Better Luck next time', 'try better next time', 'imagine losing to a non existing creature']
    msg = random.choice(messages)
    print(computer + " Beats " + choice + " So you lose. " + msg)

def draw(computer):
    if computer == 's':
        computer = 'Scissors'
        print("Draw you both picked " + computer)
        time.sleep(3)
        menu()
    elif computer == 'p':
        computer = 'Paper'
        print("Draw you both picked " + computer)
        time.sleep(3)
        menu()
    else:
        computer = 'rock'
        print("Draw you both picked " + computer)
        time.sleep(3)
        menu()

def debugmenu():
    print("Welcome to my Rock Paper Scissor Game made in python")
    time.sleep(2)
    computer = random.randint(1, 3)
    print(computer)
    choice = input("What are you choosing? Rock(R) Paper(P) or Scissors(s)")
    result(choice, computer)

if __name__ == __name__:
    menu()

