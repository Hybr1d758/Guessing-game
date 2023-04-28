import random
number = random.randint(1, 100)
print(f"computer: {number}")

print("What is your name?")
name = input()

num_of_attempts = 1 
guess = 0 
print(name + " ,this is a guess game be sure to enter number that comes to mind")

def is_even_or_odd_hint(guess: int) ->str:
    """
        return hints
    """
    even_or_odd = ""
    return f"The number computer guessed is {even_or_odd}"


while guess != number:
    print(f"Attempt{num_of_attempts}")
    guess = int(input("Enter any number:"))
    if guess == number:
        print("You're right")
        break
    elif num_of_attempts == 1:
        hint_1 = is_even_or_odd_hint(guess)
        print(hint_1)
    elif num_of_attempts == 3:
        print("You've ran out of attempts")
        break

    num_of_attempts = num_of_attempts + 1