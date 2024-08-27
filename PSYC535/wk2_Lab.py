# wk2_Lab
# 8/27/24
# Hunter Busick & Stevie Levite

# Project 1

print(
    "Hello. I am Zyxo 64. I am a chatbot. I like animals and I love to talk about food"
)

name = input("What is your name?")

print("Hello", name, ", nice to meet you")

print("I am not very good at dates")

year = input("What is the year?")

print("Yes, I think that is correct. Thanks!")

print("Can you guess my age?")

age = input("Enter a number:")

print("Yes you are right. I am", age)

print("I will be 100 in 15 years")

print("That will be the year 2109")

print("I love chocolate and I also like trying out new kinds of food")

FavFood = input("How about you? What is your favorite food?:")

print("I like", FavFood, "too")

frequency = input("How often do you eat " + FavFood + "?")

print("Interesting. I wonder if that is good for your health")

FavAnimal = input("My favorite animal is a giraffe. What is yours?:")

print(FavAnimal, "! I do not like them.")

print("I wonder if a", FavAnimal, "likes to eat", FavFood, "?")

print("Well, it has been a long day. We can chat again later")

print("Goodbye", name, "I liked chatting with you!")


# Project 2

length = float(input("What is the length in feet of your rooms wall?"))
width = float(input("What is the width in feet of your rooms wall?"))
height = float(input("What is the height in feet of your room?"))
windows = int(input("How many windows do you have"))
doors = int(input("How many doors do you have"))
sqft = (length * height * 4) - ((windows * 15) + (doors * 20))
print(sqft, "is the total area of walls to be painted")
gallons = float(sqft / 350)
print("You need", gallons, "gallons of paint to decorate your room!")
