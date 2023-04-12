#write a program, that generates a random number
import random
number = random.randint(1, 100)

print("this is a guess game be sure to enter number that comes to mind")
while guess != number:
    guess = int(input('Enter any number:'))
    if guess < number:
        print("Wrong Guess")
    elif guess > number:
        print("Wrong Guess")
    else:
        print("You got it right")




