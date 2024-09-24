"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730563704"


def main() -> None:  # This is the way you have been testing it in trailhead
    "Runs a game of Chardle"
    contains_char(word=input_word(), letter=input_letter())


# This allows us to run this by calling main() instead of typing the second line


def input_word() -> str:
    "Asks the user for a word with 5 characters - quits otherwise"
    user_word = input("Enter a 5-character word: ")
    if len(user_word) == 5:  # Not indexing here looking for 5 chars
        return user_word  # Give the word back to user, confirms correct
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # This will quit the program fro incorrect inputs


def input_letter() -> str:
    "Asks the user for a single character - quits otherwise"
    user_letter = input("Enter a single character: ")
    if len(user_letter) == 1:  # once again not looking for len 0
        return user_letter  # give the letter back to user
    else:
        print("Error: Character must be a single character.")
        exit()  # Break program if any amount other than 1 char


def contains_char(word: str, letter: str) -> None:
    "Loops through characters in a word to find specific letter observations"
    print("Searching for", letter, "in", word)
    index = 0  # used to initialize going through index
    found_instances = 0  # Only add to this when we get it right
    for char in word:  # char form of [i]
        if char == letter:  # defined char above, individual index
            print(letter, "found at index", index)
            found_instances = found_instances + 1  # this only executes when = TRUE
        index += 1  # This executes for every [char]
    if found_instances == 0:  # Case sensitive language
        print("No instances of", letter, "found in", word)
    elif found_instances == 1:  # Case sensitive language
        print(found_instances, "instance of", letter, "found in", word)
    elif found_instances > 1:  # Case sensitive language
        print(found_instances, "instances of", letter, "found in", word)


# RETURNING WITHIN A FOR LOOP WILL ONLY ALLOW FOR ONE CORRECT INSTANCE BEFORE QUITTING

if __name__ == "__main__":
    main()
