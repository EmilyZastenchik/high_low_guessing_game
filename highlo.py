import random

target = random.randint(0, 100)
print("Guess the number from 0 to 100.")


def guessMsg(guess, target):
    if(guess > target):
        print("Guess lower.")
    else:
        print("Guess higher.")
    
guess = int(input("Enter your guess: "))
counter = 0
for counter in range(0,7)  :
    

    if(guess != target): 
        guessMsg(guess, target)
        guess = int(input("Enter your guess: "))   
       
           
    counter +=1;

if(guess == target):
    print("Congrats! You got it! GAME OVER")
else:
    print("Out of Guesses! Better Luck next time.")

