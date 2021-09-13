from player import Player

class Human(Player):
    def __init__(self, lives, type, description):
        Player.lives = lives
        Player.type = type
        Player.description = description