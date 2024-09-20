"""Lab 4 Functions"""

# def reverse():
#     initiallist = list(input("What is your list?"))
#     "takes a list and reverses its order"
#     endlist = []
#     while initiallist:
#         endlist.append(initiallist.pop)
#     return endlist

card_no = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_suit = ["Clubs", "Hearts", "Diamonds", "Spades"]


def make_deck() -> list:
    "Creates a deck of cards given numbers and suits"
    deck = []
    for num in card_no:
        for suit in card_suit:
            deck.append(num + "-" + suit)
    return deck


deck = make_deck()


def card_compare(card1: str, card2: str):
    "compares two cards"
    card1 = str(input("Input your first card"))
    card2 = str(input("Input your second card"))
    if card1 and card2 in deck:
        card1index = deck.index(card1)
        card2index = deck.index(card2)
        if card1index == card2index:
            return "Your cards are the same"
        elif card1index > card2index:
            return "Card 1 higher than Card 2"
        elif card1index < card2index:
            return "Card 1 less than Card 2"
    else:
        return "One or both cards is not valid"
