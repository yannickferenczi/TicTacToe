from random import choice

class Player:
    players_turn = 0
    def __init__(self, letter):
        self.letter = letter

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def next_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val
 
class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def next_move(self, game):
        return choice(game.available_moves())

