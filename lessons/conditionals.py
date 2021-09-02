"""To demonstrate if-else conditionals."""
SECRET: int = 3

print("Try to guess this number. It's between 1 and 10.")
guess: int = int(input(" What is your guess?"))

i = 1
j = 2
while i < j:
    if guess == SECRET:
        print("Yayyy, correct!")
        print("Game over!")
        break
    elif guess > SECRET:
        print("Sorry it's incorrect. You guessed too high. Try again!")
        guess: int = int(input(" What is your guess?"))

    else:
        print("Sorry it's incorrect. You guessed too low. Try again!")
        guess: int = int(input(" What is your guess?"))
