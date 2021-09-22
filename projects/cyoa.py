"""Program that generates a random number and collects the number of attempts guess it correctly."""

__author__ = "730485647"

from random import randint

EMOJI_HAPPY: str = "\U0001F60A"  # constant 
EMOJI_PARTY: str = "\U0001F389"  # constant 
EMOJI_BYE: str = "\U0001F44B"  # constant 
points: int
player: str  


def main() -> None:
    """The main function. The program's entry point. Asks the user if they want to start the game."""
    global points  # "points" is the number of attempts a user has taken to get the correct answer
    global player
    points = 0  
    greet()
    user_choice: str = input(f"{player}, please choose(START/CONTINUE/END): ")  # Three choices
    if user_choice == "END":
        end()
    while user_choice != "END":  # Game loop
        while user_choice == "START":
            new_game()
            user_choice = input(f"{player}, please choose(START/CONTINUE/END): ")
        if user_choice == "END":
            end()
            break
        while user_choice == "CONTINUE":
            points = points + continue_game(points) + 1  # Passes the player's points value as an argument and updates the global variable "points"
            print(f"{player}! Excellent! You got it! {EMOJI_PARTY}{EMOJI_PARTY}{EMOJI_PARTY}")
            print(f"Your current adventure points: {points}")
            user_choice = input(f"{player}, please choose(START/CONTINUE/END): ")
        if user_choice == "END":
            end()
            break
        break


def greet() -> None:
    """The greet procedure. Greets the user."""
    global player
    player = input("Hello! What's your name? ")
    print(f"Hi {player} {EMOJI_HAPPY}! I hope you are doing good.\nThis is a game of guessing random numbers.\nYou'll get a hint if you don't get the answer!\nWe'll tell you how many times you've taken to get the correct answer.") 
    return


def end() -> None:
    """A custom procedure. Game ends."""
    global player
    global points
    confirm_choice: str = input(f"Are you sure you want to end the game, {player}?(YES/NO) ")
    if confirm_choice == "YES":
        print(f"Your total adventure points: {points}")
        print(f"Goodbye {player}! {EMOJI_BYE} See you next time!")
        return

    else: 
        print("Program restarting\n...\n...\n...")
        main()
    

def new_game() -> None: 
    """Another custom procedure. A new game starts."""
    global points
    global player
    points = 0
    counter: int = 0
    answer: int 
    number: int = randint(1, 10)
    print("Great! This is a new game. Take a guess. The number is between 1 and 10 (inclusive).")
    answer = int(input(f"{player}, please enter your answer here: "))
    while answer != number:
        if answer > number:
            print("Your guess is larger than the actual number.")
            answer = int(input("Try again: "))
        else:
            print("Your guess is smaller than the actual number.")
            answer = int(input("Try again: "))
        counter = counter + 1
    points = counter + 1
    print(f"{player}! Excellent! You got it! {EMOJI_PARTY}{EMOJI_PARTY}{EMOJI_PARTY}")
    print(f"Your current adventure points: {points}")
    return
    

def continue_game(a: int) -> int: 
    """A custom function. Game continues."""
    global player
    answer: int 
    counter: int = 0
    number: int = randint(1, 10)
    print("Great! This continues your last game if you've played before. Take a guess. The number is between 1 and 10 (inclusive).")
    answer = int(input(f"{player}, please enter your answer here: "))
    while answer != number:
        if answer > number:
            print("Your guess is larger than the actual number.")
            answer = int(input("Try again: "))
        else:
            print("Your guess is smaller than the actual number.")
            answer = int(input("Try again: "))
        counter = counter + 1
    return counter 


if __name__ == "__main__":
    main()
