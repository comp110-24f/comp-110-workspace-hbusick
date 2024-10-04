"""Exercise 3 Wordle"""

__author__: str = "730563704"


def main(secret: str) -> None:
    "The entrypoint of the program and main game loop."
    total_turns = 6  # Define total turns allowed
    current_turn = 1  # initialize player turn count
    while current_turn <= total_turns:  # Update index within loop
        print(
            f"=== Turn {current_turn}/{total_turns} ==="
        )  # type formatting careful throughout
        user_guess = input_guess(
            secret_word_len=len(secret)
        )  # INPUT GUESS IS LOOKING FOR INT
        game_status = emojified(
            user_guess, secret
        )  # positional arguments, gives us emojis
        print(game_status)  # print emojis for player
        if user_guess == secret:
            print(f"You won in {current_turn}/{total_turns} turns!")
            return  # win condition, return closes
        current_turn += 1  # update index over each iteration
    print(
        f"X/{total_turns} - Sorry, try again tomorrow!"
    )  # THIS GOES OUTSIDE OF THE LOOP


def input_guess(secret_word_len: int) -> str:
    word = str(input(f"Enter a {secret_word_len} character word: "))
    while len(word) != secret_word_len:  # user misinput case
        word = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
    return word  # no need for success case just return


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1  # force
    idx = 0  # initialize index
    for char in secret_word:  # char index
        if char == char_guess:
            idx += 1  # index plus 1 later if any value over 0 true
    if idx > 0:  # only has value of char ==  char_guess
        return True
    else:  # only other option case
        return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)  # force lengths
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001f7E9"  # codes
    YELLOW_BOX: str = "\U0001F7E8"
    string = ""  # initialize empty string for emojis
    idx = 0  # empty index for num characters
    while idx < len(guess):  # run condition
        if guess[idx] == secret[idx]:  # correct condition
            string += GREEN_BOX  # add green to the string
        elif contains_char(secret, guess[idx]):  # semi correct
            string += YELLOW_BOX  # add yellow to that instance of the guess
        else:
            string += WHITE_BOX  # otherwise white
        idx += 1  # increase index
    return string


if __name__ == "__main__":
    main(secret="codes")
