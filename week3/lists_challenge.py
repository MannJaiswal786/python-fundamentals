import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press Enter to pick a card, or type 'Q' and enter to quit")
    if user_input.upper() == 'Q':
        break

    selected_card = random.choice(diamonds)
    diamonds.remove(selected_card)
    hand.append(selected_card)

    print("Diamonds:", diamonds)
    print("Hand", hand)

if not diamonds:
    print("There are no more cards to pick")