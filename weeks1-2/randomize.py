import random

pips = random.randint(1, 6)
print("You roll the die...it lands with", pips, "pips showing.")

prizes = ["Car", "$10000", "$50000", "pony"]
prize_won = random.choice(prizes)
print("You turned the wheel of fortune....it lands on", prize_won + "!!")

cards = [1,2,3,4,5,6,7,8,9]
random.shuffle(cards)
print("Your cards are now shuffled in this order:")
print(cards)