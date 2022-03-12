from deck import Deck

class Shoe:

	def __init__(self, num_decks, cut):
		'''
		cut : int
				represents how many decks to leave
		'''

		self.num_decks = num_decks
		self.cut = cut
		self.shoe = self._init_shoe()
		self.cards_dealt = 0
		self.hit_cut = False

	def _init_shoe(self):
		shoe = []
		for i in range(self.num_decks):
			deck = Deck()
			deck.shuffle()
			shoe = shoe + deck.get_cards()
		return shoe

	def remove(self):
		return_card = self.shoe[0]
		self.shoe = self.shoe[1:]
		self.cards_dealt += 1
		if self.cards_dealt / 52 >= self.num_decks - self.cut:
			self.hit_cut = True
		return return_card


	def size(self):
		return len(self.shoe)

	def reset(self):
		self.shoe = self._init_shoe()