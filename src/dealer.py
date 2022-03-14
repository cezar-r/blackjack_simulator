from shoe import Shoe
from player import AdvantagePlayer

class Dealer:
	"""This class represents a dealer

	Methods
	-------
	reset()							resets the dealers hand
	get_cur_hand_display()			shows the dealers first card
	hit()							adds a card to the dealers hand
	deal()							deals each player two cards
	pop_card()						removes a card from the shoe
	get_cur_hand_rating_display()	returns the str rating of the current hand
	get_cur_hand_rating()			returns the int rating of the current hand
	get_final_rating()				returns the final rating of the dealers hand
	get_count()						returns the count
	show_card_rating()				returns the rating for the dealers first card
	"""
	def __init__(self, players):
		self.shoe = Shoe(8, 2)
		self.players = players
		self.cur_hand = []
		self._count = 0
	

	def reset(self):
		"""This method resets the dealers hand and the shoe if needed"""
		self.cur_hand = []
		if self.shoe.hit_cut:
			self.shoe = Shoe(8, 2)
			self.count = 0


	def get_cur_hand_display(self, first = False):
		"""Returns the current hand
		
		Parameters
		----------
		first:		bool
					if true, only show one card

		Returns
		-------
		list:		current hand
		"""
		if first:
			return [self.cur_hand[0], 'X']
		else:
			return self.cur_hand


	def hit(self):
		"""Recursive method to add cards to current hand until dealer hits 17"""
		card1, card2 = self.get_cur_hand_rating()
		if not card2:
			if card1 >= 17:
				return
			self.cur_hand.append(self.pop_card())
			self.hit()
		else:
			if card1 >= 17 or card2 >= 17:
				return
			self.cur_hand.append(self.pop_card())
			self.hit()


	def deal(self):
		"""Deals two cards to each player"""
		for player in self.players:
			card = self.shoe.remove()
			self._adjust_count(card)
			player.add_card(card)

		card = self.shoe.remove()
		self._adjust_count(card)
		self.cur_hand.append(card)

		for player in self.players:
			card = self.shoe.remove()
			self._adjust_count(card)
			player.add_card(card)
		
		card = self.shoe.remove()
		self._adjust_count(card)
		self.cur_hand.append(card)


	def pop_card(self):
		"""Removes a card from the shoe and returns it

		Returns
		-------
		card:		Card()
					card removed from deck
		"""
		card = self.shoe.remove()
		self._adjust_count(card)
		return card


	def get_cur_hand_rating_display(self):
		"""Returns the rating of the current hand for the display

		Returns
		-------
		str:		rating of current hand
		"""
		card1, card2 = self.get_cur_hand_rating()
		if not card2:
			return str(card1)
		return f'{card1}/{card2}'


	def get_cur_hand_rating(self):
		"""Returns the rating of the current hand

		Returns
		-------
		int, int 	rating of current hand
		"""
		rating = [0, 0]
		for card in self.cur_hand:
			rating[0] += card.value[0]
			rating[1] += card.value[1]
		if rating[0] == rating[1]:
			return rating[0], None
		else:
			if rating[0] > 21:
				return rating[1], None
			if rating[1] > 21:
				return rating[0], None
			if rating[0] == 21 or rating[1] == 21:
				return 21, None
			else:
				return rating[0], rating[1]


	def final_rating(self):
		"""Returns the final rating of the hand

		Returns
		-------
		int			rating of current hand
		"""
		card1, card2 = self.get_cur_hand_rating()
		if not card2:
			return card1
		else:
			return max(card1, card2)


	def _adjust_count(self, card):
		"""Adjusts the count based on the card passed in

		Parameters
		----------
		card: 		Card()
					card to be counted
		"""
		if card.value[1] >= 10:
			self._count -= 1
		elif card.value[1] <= 6:
			self._count += 1


	def get_count(self):
		"""Returns the count"""
		return self._count

	def show_card_rating(self):
		"""Returns the rating of the show card"""
		return self.cur_hand[0].value[1]

