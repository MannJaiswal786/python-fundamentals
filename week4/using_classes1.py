# class Player:
#     max_hp = 4000

# player1 = Player()
# print(player1.max_hp)

# Player.max_hp = 5000
# print(player1.max_hp)

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Mann", 1200)
player2 = Player("Tanishq", 1800)

print("Player1: ", player1.name, player1.hp)
print("Player2: ", player2.name, player2.hp)

