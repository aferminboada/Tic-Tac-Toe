from backend.utils import (
    get_segments,
)
from .move import Move

class Board(object):
	board = None
	who_iam = None
	moves = []

	def __init__(self, board, who_iam):
		self.board = board
		self.who_iam = who_iam
		self.segments = get_segments(board)
	
	def start(self):
		self.do_start()
		return self.choose_action()

	def do_start(self):
		self.moves = []
		for key in range(9):
			position = self.board[key]
			if position == -1: 
				# could be a move
				self.moves.append(Move(key, self.who_iam, self.segments))

	def choose_action(self):
		wins = list(filter(lambda x: x.win == True, self.moves))
		if len(wins) > 0:
			return wins[0].pos

		losses = list(filter(lambda x: x.loss > 0, self.moves))
		if len(losses) > 0:
			# need choise a best option
			return losses[0].pos

		self.moves.sort(key=lambda x: x.prob, reverse=True)
		return self.moves[0].pos
