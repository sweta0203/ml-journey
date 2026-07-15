import random

print("------------------Welcome to the number guessing game!------------------")
print(
    "Your task is to guess the number that the computer has randomly selected between 1 and 100 in about 3 attempts ."
)

# generate a random number between 1 and 100
random_number = random.randint(1, 100)
attempts = 0

# loop until the user guesses the number or runs out of attempts
while attempts < 3:
    try:
        guess = int(input("Enter your guess (between 1 and 100): "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue
    attempts += 1
    if guess < random_number:

        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(
            f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts."
        )
        break
else:
    print(
        f"Sorry, you've used all your attempts. The correct number was {random_number}. Better luck next time!"
    )
