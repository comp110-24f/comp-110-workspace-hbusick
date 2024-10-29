"""Dictionary for exercise 06"""

__author__: str = "730563704"


def invert(a: dict[str, str]) -> dict[str, str]:
    "Inverts the key and value items from dict a"
    new_dict = {}  # initialize new dictionary
    for i in a:  # for every pair in the original dictionary
        val = a[i]  # assign value of a given key i to the variable val
        if val in new_dict:  # if the current val has already been assigned to a new key
            raise KeyError("Dupe key found")  # raise an error
        new_dict[val] = i  # then add to new_dict where [val] is the key and i the value
    return new_dict  # return this new dictionary


def favorite_color(a: dict[str, str]) -> str:
    col_ct: dict[str, int] = {}  # empty dict for storing colors and their counts
    for i in a:  # for each key value pair in dict a
        color = a[i]  # assign color to that keys value
        if color in col_ct:  # if current color str already has a key in col_ct
            col_ct[color] += 1  # add 1 to the corresponding value
        else:  # otherwise
            col_ct[color] = (
                1  # define that new color with a value of 1 for this instance
            )
    count = 0  # initialize num to update when it is largest
    pop_col = ""  # initialize str for popular colorn
    for i in a:  # for every key value pair in dict a
        color = a[i]  # assign color variable to that colors str
        if col_ct[color] > count:  # if the number associated with a color is > ct
            pop_col = color  # set the popular color to that color str
            count = col_ct[color]  # and assign count to its paired num val
    return pop_col


def count(a: list[str]) -> dict[str, int]:
    empt_dict: dict[str, int] = {}  # initialize empty dict for storing
    for i in a:  # for each key value pair in a
        if i in empt_dict:  # if the value already keyed in our empty dictionary
            empt_dict[i] += 1  # find that key and add 1 to its count
        else:  # otherwise
            empt_dict[i] = 1  # create a new key value pair beginning at 1
    return empt_dict  # return this new dictionary


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}  # initialize new dictionary
    for i in a:  # for every elemennt of list a
        lead_let = i[
            0
        ].lower()  # lead_let = the 0th letter from the ith observation, ensure case
        if lead_let not in new_dict:  # if no other words have begun with this letter
            new_dict[lead_let] = (
                []
            )  # In essense create a new row in the dict with the lead let as the left
            # str - no value yet
        new_dict[lead_let].append(
            i
        )  # access the list of str's associated with the given lead_let and append the
        # i'th word to it
    return new_dict


def update_attendance(attended: dict[str, list[str]], day: str, stud: str) -> None:
    if day not in attended:  # if day does not exist in attended dict
        attended[day] = []  # initialize new list for day
    if stud not in attended[day]:  # if a student has not had their attendece recorded
        attended[day].append(stud)  # append that str value to corresponding day
