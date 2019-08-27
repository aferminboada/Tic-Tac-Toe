from random import randint
from backend.moves import Board as start_play_pc
from backend.utils import (
    clean_positions,
    a_winner,
)
from backend.messages import (
    start_player,
    start_pc,
    mov_available,
    winner,
)


class Play(object):
    how_begin = None
    computer = None
    player = None
    turn_of = None
    board = None
    movements = 0

    def do_start(self, **options):
        self.computer = options.get('computer', 'PC')
        self.player = options.get('player', 'PLAYER')
        self.choose_how_begin()
        self.clear_game()
        exist_a_winner = self.start()
        self.show_board()
        if exist_a_winner is None:
            print("Tie")
            return None

        print(winner, self.pc if exist_a_winner else self.player)
        print("-------------------------")

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
            opt = start_play_pc(self.board, mark).start()
            # no define movement
            # opt = self.wait_move_player()
        else:
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
