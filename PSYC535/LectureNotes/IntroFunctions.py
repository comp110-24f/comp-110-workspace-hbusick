"""Introduction to Functions"""

# Refresher on nested loops

# days = ["M", "T", "W", "TH", "F"]
# Tasks = ["Shower", "Breakfast", "Feed Cat", "Brush Teeth"]

# for day in days:
#     print("Tasks for", day)
#     for task in Tasks:
#         print("o ", task)

#     print()


stim_list = ["dog", "horse", "cow", "pig", "cat"]
q_list = ["clear", "detailed", "colorful"]

for stim in stim_list:
    print("Think of a", stim)
    for q in q_list:
        print("How", q, "is the image?")


def hello():
    print("Hello World")


def hellotoyou(name):
    print("Hello", name)
