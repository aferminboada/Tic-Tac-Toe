from random import randint
from backend.moves import move
from backend.utils import (
    clean_positions,
    a_winner,
)
from backend.messages import (
    start_player,
    start_pc,
    mov_available,
)


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
        exist_a_winner = self.start()
        if exist_a_winner is None:
            print("draw")

        print("winner ", exist_a_winner)

    def choose_how_begin(self):
        self.how_begin = randint(0, 1)  # 0 is PLAYER, 1 is PC
        self.turn_of = self.how_begin
        if self.how_begin:
            print(start_pc.format(computer=self.computer))
        else:
            print(start_player.format(player=self.player))

    def clear_game(self):
        self.board = [-1]*9
        self.movements = 0

    def start(self):
        # if is turn of pc /moves.move decide the move
        # if is turn of player show the board and wait for input
        self.show_board()
        mark = 'X' if self.how_begin == self.turn_of else 'O'
        if self.turn_of:
            opt = self.wait_move_player()
        else:
            # no define movement
            # opt = move(self.board, self.movements, mark)
            opt = self.wait_move_player()

        # any code here
        self.board[opt] = mark
        if a_winner(self.board):
            return self.turn_of
        if self.movements == 8:
            return

        self.turn_of = not self.turn_of
        self.movements += 1
        return self.start()

    def wait_move_player(self):
        _clean_positions = clean_positions(self.board)
        try:
            move = int(input("movimiento: "))
            if move not in _clean_positions:
                raise NameError('')
            return move-1
        except:
            print(mov_available.format(pos=_clean_positions))
            return self.wait_move_player()

    def show_board(self):
        print("-----------------------")
        for i in range(0, 9):
            x = i + 1
            print(" ", self.board[i] if self.board[i] != -1 else (i+1), " ", end='')
            if x % 3 == 0:
                print()
        print("-----------------------")
