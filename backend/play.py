from random import randint
from backend.messages import start_player, start_pc
from backend import move


class Play(object):
    how_begin = None
    computer = None
    turn_of = None
    board = None
    movements = 0

    def __init__(self, options):
        self.debug = options.get('debug')
        self.computer = options.get('computer')
        self.player = options.get('player')
        self.choose_how_begin()
        self.do_start()

    def do_start(self):
        self.clear_game()
        a_winner = self.start()
        if a_winner is None:
            print("draw")

        print("winner ", a_winner)

    def choose_how_begin(self):
        self.how_begin = randint(0, 1)  # 0 is PLAYER, 1 is PC
        self.turn_of = self.how_begin
        if self.how_begin:
            print(start_pc.format(computer=self.computer))
        else:
            print(start_player.format(player=self.player))

    def clear_game(self):
        self.board = (-1)*9
        self.movements = 0

    def start(self):
        # if is turn of pc /moves.move decide the move
        # if is turn of player show the board and wait for input

        # any code here

        if self.a_winner():
            return self.turn_of
        if self.movements == 9:
            return

    def a_winner(self):
        # find if exist any winner
        raise NotImplementedError()
