from random import randint
from time import sleep

def replay():
    i = input("Do you wish to play again type Y to continue or N to not : ").lower()
    if i == "y":
        ti()
    else:
        sleep(2)
        exit()

def task(l , h):
    no = randint(l , h)
    chances = round((h+l)/2)
    print(f"You have {chances} to find the number")
    while chances != 0:
        chances -= 1
        print(f"You have {chances} left")
        try:
            guess = int(input("Guess the number : "))
        except:
            print("Pease enter number only")
            chances += 1
            continue
        if guess == no:
            print("Congratulations !! \n You Win !! \n Do you wish to play again ?")
            replay()
        elif no - guess >= 1 and no - guess <= 5:
            print("Too close")
        elif guess - no >= 1 and guess - no <= 5:
            print("Too close")
        elif chances == 0 and guess != no:
            print(f"You loose!! \n The number was {no} \n Better luck next time... \n Would you like to play again")
            replay()
        else:
            print("That is not the number")

def checking(l , h):
    if l == 0 and h == 0:
        print("Both the numbers cant be 0")
        ti()
    elif l > h:
        print("Lower number cant be greater than higher number")
        ti()
    elif l == h:
        print("Both the numbers cant be equal.")
        ti()
    elif l < h and h - l == 10:
        task(l , h)
    elif l < h and h - l > 10:
        task(l , h)
    else:
        print("There should be minimum gap of 10 between higher and lower number")
        ti()

def ti():
    ln = input("Enter the lower number : ")
    hn = input("Enter the higher number : ")
    if ln == "" and hn == "":
        print("Please enter some numbers")
        ti()
    elif ln == "" and hn != "":
        ln = "0"
    elif ln != "" and hn == "":
        hn = "0"
    try:
        ln = int(ln)
        hn = int(hn)
        checking(ln , hn)
    except:
        print("You should only enter integer values")

def wish():
    print("Welcome to guessing game !!")
    print("In this game you have to provide the computer a range , then the computer will select a random number between that range , you have to guess number.")
    ti()

wish()