from .defense import (
	get_positions, 
	i_can_win, 
	i_will_win,
	get_attack_coefficient,
)


class Move(object):
	pos = None
	who_iam = None
	win = False
	loss = 0
	prob = 0.0
	segments = None

	def __init__(self, pos, who_iam, segments):
		self.pos = pos
		self.who_iam = who_iam
		self.segments = segments
		self.positions = get_positions(self.pos)
		self.i_could_win()
		self.i_could_loss()
		self.get_prob()

	def i_could_win(self):
		# find if i could win the game
		
		for pos in self.positions:
			if i_can_win(self.segments[pos], self.who_iam):
				self.win = True
				return 

	def i_could_loss(self):
		# find if i could loss the game
		self.loss = get_attack_coefficient(self.segments, self.positions, self.who_iam)

	def get_prob(self):
		cant = 4 # max number of possibilities
		wins = 0
		for pos_segment in self.positions:
			if i_will_win(self.segments[pos_segment], self.who_iam):
				wins += 1

		self.prob = (float(wins) / cant) * 100
