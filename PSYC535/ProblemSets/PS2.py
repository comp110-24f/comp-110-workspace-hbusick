"""Problem Set 2"""

# Guess my number! Choose a secret number that the users shall guess
# Users have 3 guesses to get my number between 1-20
# For each guess, tell me whether my number is correct, too high,
# or too low. Only give the user more guesses if they are wrong initially

# HINT: It may be helpful to use nested if statements here!!

number = int(16)

number1 = int(input("What is your first guess?"))

if number1 == number:
    print("Correct!")
else:
    if number1 > number:
        print("Too high")
    else:
        print("Too low")
    number2 = int(input("What is your second guess?"))
    if number2 == number:
        print("Correct!")
    else:
        if number2 > number:
            print("Too high")
        else:
            print("Too low")
        number3 = int(input("What is your final guess?"))
        if number3 == number:
            print("Correct!")
        else:
            if number3 > number:
                print("Too high, you loose")
            else:
                print("Too low, you loose")

# if number1 == number:
#     print("Correct!")
#     exit()
# else:
#     if number1 > number: ###Broken
#         print("Too high")
#     else:
#         print("Too low")

# number2 = int(input("What is your second guess?"))

# if number2 == number:
#     print("Correct!")
#     exit() ##################Broken
# else:
#     if number2 > number:
#         print("Too high")
#     else:
#         print("Too low")

# number3 = int(input("What is your final guess?"))

# if number3 == number:
#     print("Correct!")
# else:
#     if number3 > number:
#         print("Too high, you loose") ################Broken
#     else:
#         print("Too low, you loose")


# Some help for a budding biologist:
# here, the user will input a DNA base
# your task is to print the complementary base to them (A - T, G - C)
# include a case for the scenario where the user enters something wrong!

DNABase = str(input("Input a DNA Base"))

if DNABase == "A":
    print("Your Compliment Base is T")
elif DNABase == "T":
    print("Your Compliment Base is A")
elif DNABase == "G":
    print("Your compliment base is C")
elif DNABase == "C":
    print("Your Compliment base is G")
else:
    print("Invalid input, did you make sure to capitalize your base?")

"""Create a dog or cat to human age calculator. Problem taken from Creative
Coding in Python, by Sheena Vaidyanathan"""

# things to note about dog ages:
#   1st dog year = 12 human years
#   2nd dog year = 24 human years
#   Add 4 years for every dog year after that

# things to note about cat ages:
#   1st cat year = 15 human years
#   2nd cat year = 24 human years
#   Add 4 years for every cat year after that

# Sample run:
#   >>> Enter dog or cat: cat
#   >>> Enter age of animal: 4
#   >>> Human age of cat is 32


Dog_or_Cat = str(input("Do you have a Dog or a Cat? (Enter Dog or Cat)"))

if Dog_or_Cat == "Dog":
    dog_age = int(input("How many years old is your Dog?"))
elif Dog_or_Cat == "Cat":
    cat_age = int(input("How many years old is your Cat?"))
else:
    print("Input not recognized, is your case correct?")

# if dog_age == 1:
#     print("Your Dog is 12 in human years!")
# elif dog_age == 2:
#     print("Your Dog is 24 in human years")
# elif dog_age > 2:
#     dog_age2 = ((dog_age - 2) * 4) + 24
#     print("Your Dog is", dog_age2, "in human years!")

# if cat_age == 1:
#     print("Your Cat is 15 in human years!")
# elif cat_age == 2:
#     print("Your Cat is 24 in human years") "This chunk and the one above are wrong
# elif cat_age > 2:
#     cat_age2 = ((cat_age - 2) * 4) + 24
#     print("Your Cat is", cat_age2, "in human years!")

if Dog_or_Cat == "Dog":
    if dog_age == 1:
        print("Your Dog is 12 in human years!")
    elif dog_age == 2:
        print("Your Dog is 24 in human years")
    elif dog_age > 2:
        dog_age2 = ((dog_age - 2) * 4) + 24
        print("Your Dog is", dog_age2, "in human years!")
else:
    if cat_age == 1:
        print("Your Cat is 15 in human years!")
    elif cat_age == 2:
        print("Your Cat is 24 in human years")
    elif cat_age > 2:
        cat_age2 = ((cat_age - 2) * 4) + 24
        print("Your Cat is", cat_age2, "in human years!")

"""Inspired by the show 'The Good Place': You are in charge of deciding where people
go in the afterlife, and your options are either to send them to the 'The Good Place'
or 'The Bad Place.' You have a list of people that are definitely bad. For everyone
else, you must determine whether their overall goodness score is enough to let them
into The Good Place. A score of over 1 thousand will get you into The Good Place."""

# Ask for the person's name.
# Choose some inputs you want to collect to determine a person's score.
# Ask the user a series of y/n questions based on your created criteria.
# ^ This is entirely up to you! You can assign +/- points to certain life skills,
# achievements, etc. based on what you see fit
# For example, maybe Holding the door open for others is worth 100 points
# and Dining and dashing is worth -500 points

# If the person is in the bad list, they go to The Bad Place, no matter what.
# Otherwise, make necessary calculations/judgments based on their answers to the above.
# Tell the person (gently) where they end up

# Definitely bad people (feel free to add names as you see fit):
bad_list = ["Robot Devil", "Dolores Umbridge", "Dracula", "Scar", "Emperor Palpatine"]

print("Today we decide your fate!")
name = str(input("What is your name?"))
print(
    "Okay",
    name,
    ", I have some questions for you. Please answer Y for yes and N for no",
)

point_value = 0

class_attend = str(input("Did you attend PSYC 535 regularly?"))

if class_attend == "Y":
    point_value = point_value + 100
else:
    point_value = point_value - 100

patient = str(input("Were you a patient person?"))

if patient == "Y":
    point_value = point_value + 200
else:
    point_value = point_value - 200

honest = str(input("Were you an honest person?"))

if honest == "Y":
    point_value = point_value + 300
else:
    point_value = point_value - 300

inprisoned = str(input("were you ever inprisoned?"))

if inprisoned == "Y":
    point_value = point_value - 1000
else:
    point_value = point_value + 1000

if name in bad_list:
    print("Regardless of your points you must go to The Bad Place")
else:
    if point_value < 1000:
        print("Your points suggest you go to The Bad Place")
    else:
        print("Your points suggest you go to The Good Place")


"""The point of this problem is to help you get comfortable manipulating lists.
Simply follow the steps below using code and print your final results as suggested."""


# Create an empty list named numbers.
# Add the numbers 5, 10, 15, 20, and 25 to the list in that order.
# Print the list.
# Insert the number 12 at index 2.
# Remove the number 15 from the list.
# Find and print the index of the number 20 in the list.
# Check if the number 10 is present in the list and if so, move it to the back.
# Print your final list

# Here's what your output should look like:
# [5, 10, 15, 20, 25]
# 20 is now at index 3
# Our final list looks like: [5, 12, 20, 25, 10]


numbers = []

numbers = [5, 10, 15, 20, 25]

print(numbers)

numbers.insert(2, 12)

numbers.remove(15)

print("20 is at index", numbers.index(20))

if 10 in numbers:
    numbers.remove(10)
    numbers.append(10)

print(numbers)
