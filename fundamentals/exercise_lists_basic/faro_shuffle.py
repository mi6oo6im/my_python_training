deck_of_cards = input().split()
number_of_shuffles = int(input())
middle_of_deck = len(deck_of_cards) // 2
for _ in range(number_of_shuffles):
    shuffled_deck = []
    left_deck = deck_of_cards[:middle_of_deck]
    right_deck = deck_of_cards[middle_of_deck:]
    for i in range(len(left_deck)):
        shuffled_deck.append(left_deck[i])
        shuffled_deck.append(right_deck[i])
    deck_of_cards = shuffled_deck
print(deck_of_cards)

