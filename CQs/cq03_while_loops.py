"""While Loops Challenge Question"""

__author__ = "730563704"


def num_instances(phrase: str, search_char: str) -> int:
    "Counts the number of instances a character appears in a phrase"
    count = 0  # Initial value of number of correct character observations
    index = 0  # Intial value of the index in phrase, will add 1 with each loop
    while index < len(phrase):  # Add 1 to index until it exceeds the length of phrase
        if phrase[index] == search_char:  # If a specific character == our lookup value
            count += 1  # Add one to count if the above statement is true
        index += 1  # No matter what each time we loop add to indec
    return count  # Return value once loop concludes
