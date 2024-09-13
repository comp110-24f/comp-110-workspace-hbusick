"""Challenge Question no.2 COMP 110 FA24"""

__author__ = "730563704"


def guess_a_number() -> None:
    "Plays a game of guessing a secret number"
    secret = int(7)
    guess = int(input("Guess a number:"))
    print("Your guess was", guess)
    if secret == guess:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    elif guess > secret:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
