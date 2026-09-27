import random

number = random.randint(1, 100)

print("Guess the Number Game")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")
        break
