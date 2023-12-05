deck_of_cards = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    middle_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_deck]
    right_part = deck_of_cards[middle_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):    # Right part
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling
print(deck_of_cards)