"""Third problem set"""

# Problem 1
# Extend your DNA base return problem from last week
# Now, the user can enter a DNA list as long as they want, e.g. AGCTATCG
# You must return the corresponding complement for the set of bases
# Print the final result all as a single string, e.g. 'TCGATAGC'
# Hint, an empty string is simply ''

user_string = str(input("Input your DNA base"))
empty_string = []

for dna in user_string:
    if dna == "A":
        empty_string.append("T")
    elif dna == "T":
        empty_string.append("A")
    elif dna == "C":
        empty_string.append("G")
    elif dna == "G":
        empty_string.append("C")
    else:
        print("Incorrect base entered")

print("Your compliment string is", empty_string)


# Problem 2

# You are cleaning up some code from a friend, and you see the following program:

# list1 = [3, 24, 17, 9, 36]
# print(list1)

# count = 0
# list2 = []
# total = len(list1)
# while count < total:
#     print(list1[count] - 5)
#     list2.append(list1[count] - 5)
#     count += 1
# print(list2)

# math = 0
# for i in list2:
#     math = math + i * 2
# print(math)

# Your task is to figure out what this code is doing and to rewrite it more
# cleanly and clearly. Justify your decisions as comments accompanying your code


list1 = [3, 24, 17, 9, 36]
print(list1)

for i in range(len(list1)):
    # for every observation in the entire length of list 1
    list1[i] = list1[i] - 5
# take the ith observation and replace it with the ith observation -5
# this way we condense the code and lessen how many variables we need

print(list1)

math = 0
for i in list1:
    math = math + i * 2
print(math)

# running the math function now on list1 produces the same result


# Problem 1
# Create a factorial solver (without using the factorial function!)
# Get the input of an integer
# Print its factorial

integer = int(input("Type a whole number"))
base = 1  # anything times 0 = 0 -> initialize

while integer > 1:  # decreasing by 1 in each iteration
    base = base * integer  # the number we are continually adjusting
    integer = integer - 1  # makes loop run integer times

print(base)

# Problem 2
# Find the sum and average value of a list of numbers
# I will provide a list below, but it should work regardless of the values in
# my_list (should work with any generic list of numbers)

my_list = [1, 2, 3, 4, 5, 6]
initialize = 0

for i in range(len(my_list)):
    initialize = initialize + my_list[i]

print("The sum of your list is", initialize)

len_my_list = len(my_list)

avg = initialize / len_my_list

print("The average of your list is", avg)

# Part 1
# The goal: take in variable input from the user and put it all into a list
# Ask the user how many items they would like to enter
# Take each item in one at a time and print at the end in one list
# You can treat all input items as strings; no need to convert

# Sample run:
# >>> How many items would you like to enter?: 2
# >>> Item 1
# >>> Enter your item: a
# >>> Item 2
# >>> Enter your item: 84


num_inputs = int(input("How many items would you like to enter?: "))
empty_str = []


while num_inputs > 0:
    q_input = input("enter your item")
    empty_str.append(q_input)
    num_inputs = num_inputs - 1

print("your list is:", empty_str)


# Part 2
# Create a program that takes the final list from part 1 and gives us a version
# of that list without any duplicates. Essentially, it prints out a new list
# including only the unique items

# Example:
# list_from_above = ['a', 'b', 'c', 'a', 'c', 'd']
# Output: Your uniquified list is ['a', 'b', 'c', 'd']

# Hint: You can take advantage of the break/continue commands we learned!

empty_str_NoDupe = []

for i in empty_str:
    if i not in empty_str_NoDupe:
        empty_str_NoDupe.append(i)

print(empty_str_NoDupe)
