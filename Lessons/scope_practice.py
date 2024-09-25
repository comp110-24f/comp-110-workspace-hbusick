"""Practice with scope and Global Variables"""


def remove_chars(msg: str, char: str) -> str:
    "Return a copy of msg with all instances of char removed"
    copy: str = ""  # set up empty copy string
    index = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":  # These lines will be ignored when importing
    word = "yoyo"
    print(
        remove_chars(word, char="y")
    )  # word is a positional argument thus no = necessary
