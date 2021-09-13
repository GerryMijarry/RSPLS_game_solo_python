from human import Human
from ai import Ai

import random

class Game:
    def __init__(self):
        self.player1 = Human(3, "Human", "Human 1")
        self.player2 = Ai(3, "AI (Computer)", "Computer")
        self.weapon = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def run_game(self):
        self.display_welcome()
        self.play_game()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        player2 = int(input("Will the second player be a human [Press 1] or [Press 2] to play the AI?"))
        if player2 == 1:
            self.player2 = Human(3, "Human", "Human 2")
        if player2 == 2:
            pass
        
    def play_game(self):
        while self.player1.lives > 0 and self.player2.lives > 0:
            self.player_turn()
                
        
    def player_turn(self):
        self.show_player_options()
        player1_weapon = int(input("What weapon will Player 1 use"))
        self.show_player_options()
        if self.player2.type == "AI (Computer)":
            player2_weapon = self.weapon[random.randint(1, 5)]
        elif self.player2.type == "Human":
            player2_weapon = int(input("What weapon will Player 2 use?"))

        if player1_weapon == "Rock": 
            if player2_weapon == "Rock":
                print(f"Both players selected {player1_weapon}. It's a tie!")
            elif player2_weapon == "Paper":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_weapon} wraps around {player1_weapon}!")
                self.player1.lives -= self.player1.lives
            elif player2_weapon == "Scissors":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_weapon} smashes {player2_weapon}!")
                self.player2.lives -= self.player2.lives
            elif player2_weapon == "Lizard":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_weapon} crushes {player2_weapon}!")
                self.player2.lives -= self.player2.lives
            elif player2_weapon == "Spock":
                print(f"{self.player2.description} beats {self.player1.description} since {player1_weapon} vaporizes {player2_weapon}!")
                self.player1.lives -= self.player1.lives

        

        

        



    def show_player_options(self):
        print("Make sure your opponent isn't watching and select your weapon!")
        counter = 0
        for weapon in self.weapons:
            print('Press ' + str(counter) + ' to select ' + weapon)
            counter +=1

    def display_winners(self):
        if len(self.player1.lives) > len(self.player2.lives):
            print('Player 1 wins!!')
        else:
            print('Player 2 wins!')
