
from shoe import Shoe
from player import AdvantagePlayer

class Dealer:

	def __init__(self, players):
		self.shoe = Shoe(8, 2)
		self.players = players
		self.cur_hand = []
		self._count = 0
	

	def reset(self):
		self.cur_hand = []
		if self.shoe.hit_cut:
			self.shoe = Shoe(8, 2)
			self.count = 0

	def get_cur_hand_display(self, first = False):
		if first:
			return [self.cur_hand[0], 'X']
		else:
			return self.cur_hand

	def hit(self):
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
		card = self.shoe.remove()
		self._adjust_count(card)
		return card

	def get_cur_hand_rating_display(self):
		card1, card2 = self.get_cur_hand_rating()
		if not card2:
			return str(card1)
		return f'{card1}/{card2}'


	def get_cur_hand_rating(self):
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
		card1, card2 = self.get_cur_hand_rating()
		if not card2:
			return card1
		else:
			return max(card1, card2)




	def _adjust_count(self, card):
		if card.value[1] >= 10:
			self._count -= 1
		elif card.value[1] <= 6:
			self._count += 1

	def get_count(self):
		return self._count

	def show_card_rating(self):
		return self.cur_hand[0].value[1]




players = [AdvantagePlayer('Cezar')]

if __name__ == '__main__':
	dealer = Dealer(players)