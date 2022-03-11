from cards import Card, VALUES
import random



class Deck:

	def __init__(self):
		self.deck = self._init_deck()

	def _init_deck(self):
		deck = []
		for i in range(4):
			for card in VALUES:
				deck.append(Card(card))
		return deck

	def shuffle(self):
		random.shuffle(self.deck)

	def get_cards(self) -> list:
		return self.deck