"""Concatenation function for cq04"""

__author__ = "730563704"


def concat(str1: str, str2: str) -> str:
    "Concatenates two strings into one"
    store: str = ""  # initialize empty string
    store = str1 + str2  # add both strings to empty string
    return store  # return now nonempty str


word1: str = "happy"  # globals
word2: str = "tuesday"

if __name__ == "__main__":  # only runs in this module bc of name main
    print(concat(word1, word2))
