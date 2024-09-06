# password = "password"

# user_input = input("What is your password?")

# if password == user_input:
#     print("Access Granted")
# else:
#     print("Incorrect Password")


# sideA = int(input("How long is side A?"))
# sideB = int(input("How long is side B?"))
# sideC = int(input("How long is side C?"))

# if sideA == sideB == sideC:
#     print("You have an equilateral triangle!")
# else:
#     if (
#         (sideA == sideB) & (sideC != sideA & sideB)
#         or (sideA == sideC) & (sideB != sideA & sideC)
#         or (sideC == sideB) & (sideA != sideC & sideB)
#     ):
#         print("You have an isosceles triangle!")
#     else:
#         print("You have a scalene triangle")


# Create a morning outfit/packing helper
# Ask the user a series of questions:
#     Is it rainy out (y or n)
#     What is the temperature (int or float)
#     Do you own an umbrella (y or n)
#     Is it a weekend day (y or n)
# Based on this information, determine if the user needs:
#     To leave the house at all (do they have school today?)
#     If so, do they wear rainboots? Should they take an umbrella?
#     Whether to wear shorts or pants (temperature above a certain level)
# Feel free to add other questions/decisions!

rainy = str(input("Is it raining today? Y/N"))
umbrella = input("Do you have an umbrella? Y/N")
temp = int(input("What is the temperature outside?"))


day = str(input("Is it a weekend day? Y/N"))

if day == "Y":
    print("You do not have school today!")
else:
    print("You have school today")

rainy = str(input("Is it raining today? Y/N"))
