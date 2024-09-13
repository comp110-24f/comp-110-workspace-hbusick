# Problem 1
# print a list of all numbers between 1200 and 2700 that are
# divisible by 7 and a multiple of 5

numbs = list(range(1200, 2701))

for i in numbs:
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Problem 2
# print the numbers of the Fibonacci series from 0 to 50
# Note: the Fibonacci series is one where each number is the sum of the
# 2 numbers before it, i.e. 1, 1, 2, 3, 5, 8,...
# Try to use a while loop here! Also, feel free to manually code the first couple
# numbers in the sequence to get the code going!

x = 0
num1 = 1
num2 = 1
nex_num = num2

print(1)
print(1)
while x < 50:
    x = num1 + num2
    num1 = num2
    num2 = x
    print(x)


# Create a quiz game that gives you a score at the end of the quiz.

# I am providing you with the questions and the answers
# in the form of two lists. You must use these lists in your code
# (that means, do not rewrite the text from these lists in your
# code separately)

# HINT: use the fact that the question and answer are at the same index
# for the two lists. So, it might be easier to loop through index values
# rather than the lists themselves!

# Sample Run (just the first 2 questions):
#   >>> What is the capital of Peru? Lima
#   >>> You are correct
#   >>> What is the chemical formula for table salt? H20
#   >>> You are incorrect
#   >>> The correct answer is NaCl
#   ...
#   >>> Your score is 1

# here are some things to get you started
question_list = [
    "What is the capital of Peru?",
    "What is the chemical formula for table salt?",
    "What animal is the largest living creature on Earth?",
    "Who painted the ceiling of the Sistine Chapel?",
    "How many bones does an adult human have?",
]

answer_list = ["Lima", "NaCl", "whale", "Michelangelo", "206"]

score = 0

print(question_list)

Q1 = str(input("Answer for Q1"))
Q2 = str(input("Answer for Q2"))
Q3 = str(input("Answer for Q3"))
Q4 = str(input("Answer for Q4"))
Q5 = str(input("Answer for Q5"))

user_answers = [Q1, Q2, Q3, Q4, Q5]

for i in range(len(answer_list)):
    if answer_list[i] == user_answers[i]:
        print("Correct")
        score = score + 1
    else:
        print("The correct answer is", i)
        score = score - 1

print(score)
