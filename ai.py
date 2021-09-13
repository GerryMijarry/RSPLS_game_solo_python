from player import Player

class Ai(Player):
    def __init__(self, lives, type, description):
        Player.lives = lives
        Player.type = type
        Player.description = description



