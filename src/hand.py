


class Hand:

	def __init__(self, hand = []):
		self.init()
		self.hand = hand

	def __str__(self):
		return_str = ''
		for card in self.hand:
			return_str += f'{card} '
		return return_str[:-1]

	def init(self):
		self.hand = []
		self.stood = False
		self.blackjack = False
		self.bust = False
		self.is_soft = False
		self.rating = self._init_rating()


	def _init_rating(self):
		if not self.hand:
			return [0, 0]
		else:
			return self.hand[0].value


	def is_paired(self):
		if len(self.hand) == 2:
			if self.hand[0].value[0] == self.hand[1].value[0]:
				return True
		return False


	def add_card(self, card):
		self.hand.append(card)
		self.rating[0] += card.value[0]
		self.rating[1] += card.value[1]

		card1, card2 = self._get_rating()
		if not card2:
			if card1 == 21:
				self.blackjack = True
			elif card1 > 21:
				self.bust = True
		else:
			self.is_soft = True

	def stand(self):
		self.stood = True

	def get_rating(self):
		card1, card2 = self._get_rating()
		if not card2:
			return card1
		else:
			return f'{card1}/{card2}'


	def get_final_rating(self):
		card1, card2 = self._get_rating()
		if not card2:
			return card1
		else:
			return max(card1, card2)

	def _get_rating(self):
		if len(self.rating) == 1:
			return self.rating[0], None

		if self.rating[0] == self.rating[1]:
			return self.rating[0], None

		else:
			if self.rating[0] > 21:
				return self.rating[1], None
			if self.rating[1] > 21:
				return self.rating[0], None
			if self.rating[0] == 21 or self.rating[1] == 21:
				return 21, None
			else:
				return self.rating[0], self.rating[1]

	def split_cards(self):
		return self.hand[0], self.hand[1]

