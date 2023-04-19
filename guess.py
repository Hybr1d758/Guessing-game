#write a program, that generates a random number
import random
number = random.randint(1, 100)

print("What is your name?")
name = input()

guess_count = 4
guess = 0
print(name + ", this is a guess game be sure to enter number that comes to mind.")
while guess < 4:
    guess = int(input('Enter any number:'))
    if guess % 2:
        print("The answer is an odd number")
    else:
        print("The answer is an even number")
        break
    if guess > number:
        print("The answer is lower than the number")
    else:
        print("The answer is greater than the number")        
        break
    if guess == number:
        print("Well done, you got it right")
    else:
        print("Wrong answer! you have run put attempts")
    
     



