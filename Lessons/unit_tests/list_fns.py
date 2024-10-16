"""Writing three functions for class"""


def get_first(input: list[str]) -> str:
    "Return first element"
    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    var: str = input[0]
    input.pop(0)
    return var
