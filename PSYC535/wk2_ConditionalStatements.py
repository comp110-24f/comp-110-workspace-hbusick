"""Week 2 Thursday Lecture on Intro to Conditional Statments"""

# a Boolean is returns either true or false and commonly use operators such
# as >, <, =, != and others


# "Code that returns true if a bag is equal to or over 50lbs (overweight)"
# Bag_Weight = float(input("How heavy is your bag in pounds?"))
# print(Bag_Weight > 50)

# number = input("type a whole number")
# remainder = int(number) % 2
# if remainder == 0:
#     print("your number is even")
# else:
#     print("your number is odd")


# Bag_Weight2 = float(input("How heavy is your bag in pounds"))
# Ammt_Over = Bag_Weight2 - 50
# if Bag_Weight2 > 50:
#     print("Your bag is overweight by", Ammt_Over, "lbs")
# else:
#     print("Your bag is OK")


# A list in python is a combination of data separated by commas and within brackets
# [1,2,3,4,5,6]
# can store the info in a variable
# x = [2,3,4]
# can conbine different data types
# [2, 'hello', 23.4, True]
# indexing starts at 0 in python

distance = int(input("What is your distance?"))
if distance <= 5:
    print("Amazing you get 50 points")
elif distance <= 50:
    print("you get 5 points")
elif distance <= 15:
    print("you get 15 points")
else:
    print("sorry no points")


if distance <= 5:
    print("yes")
else:
    print("no")
