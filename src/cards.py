

VALUES = ['2', '3', '4', '5', '6', '7' ,'8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:

	def __init__(self, rank):
		self.rank = rank
		self.value = self._calc_value()

	def _calc_value(self):
		if self.rank == 'J':
			return [10, 10]
		elif self.rank == 'Q':
			return [10, 10]
		elif self.rank == 'K':
			return [10, 10]
		elif self.rank == 'A':
			return [1, 11]
		else:
			return [int(self.rank), int(self.rank)]

	def __str__(self):
		if self.rank[0] != 1:
			return f'{str(self.rank)}'

	def __repr__(self):
		return f'{self.rank}'