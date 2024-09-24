"""Python Overview Review"""

participant_ratings = [[4, 5], [1, 2, 3], [1], [7, 3, 8, 2, 4]]

for inner_list in participant_ratings:
    length = len(inner_list)
    index = participant_ratings.index(inner_list)

    print("Participant", index, "has", length, "items")

    total = 0
    for value in inner_list:
        total += value

    average = total / length
    print("Participant", index, "got a score of", average)
