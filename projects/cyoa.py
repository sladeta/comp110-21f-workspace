"""Create my own number guessing game."""

__author__ = "730236019"

from random import randint

points: int = 0 
player: str = ""
YIKES: str = '\U0001F62C'
TEAR: str = '\U0001F62A'
COWBOY: str = '\U0001F920'


def main() -> None:
    """The program's entrypoint."""
    greet()
    proceed()


def greet() -> None:
    """A Greeting for my game."""
    global player
    player = input("Hello mi amigo. What is your name? ")
    print("Welcome to Slade's Famous Coin Flip Game, " + player + "!")
    print("In this game, the software will flip a standard coin. Your goal is to guess heads or tails correctly, and the game will keep score! ")


def proceed() -> None: 
    """Allows the player to either enter the game or to decline based on instructions."""
    response: int = int(input("Would you like to play? (1 for Yes, 2 for No): "))
    if response == 1:
        game()
    else:
        end()


def game() -> None: 
    """The actual coin game."""
    options: int = int(input("Heads or Tails? (1 for heads, 2 for tails, 3 for score): "))
    answer: int = randint(1, 2)
    global points
    if options == answer:
        points += 1
        print(f"Correct. You now have {points} points! ")
        game()
    else:
        if options == 3:
            points = score(points)
            game()
        else:
            print(f"Incorrect {YIKES}. Better luck next time. ")
            print(f"Your final score: {points} points")
            points = 0 
            proceed()


def score(x: int) -> int:
    """Allows the player to view points, then clear points or continue on."""
    print(f"Why hey there fellar {COWBOY}. Current Score: {x} points")
    clear: int = int(input("Press 1 to clear out those points of yours, any other number to keep playing: "))
    if clear == 1:
        x = 0
    return x
   

def end() -> None:
    """A goodbye message to any departing player."""
    global name
    print(f"You earned: {points} points! ")
    print(f"Thanks for playing! Goodbye {TEAR}, {player}. ")


if __name__ == "__main__":
    main()