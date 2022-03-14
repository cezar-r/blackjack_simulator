
from hand import Hand
from strategy import *


TRUE_COUNT_STRATEGY = {
	2 : 25,
	3 : 50,
	4 : 75,
	5 : 100,
	6 : 125,
	7 : 150,
	8 : 175,
	9 : 200,
	10 : 225,
	11 : 250
}

NORMAL_BET_SIZE = 10

class AdvantagePlayer:
	"""This class represents an advantage player

	Methods
	-------
	add_card()					adds a card to the players hand
	hit()						adds a card to the players hand at index idx
	stand()						player stands
	split()						player splits
	double_down()				player doubles down
	get_cur_hand_rating()		gets the rating of the current hand
	evaluate_count				adjusts bet size based on count
	decision					retuns a decison based on current hand and dealers hand
	"""
	def __init__(self, name, balance = 10_000):
		self.name = name
		self.cur_hand = [Hand()]
		self.balance = balance
		self.bet_size = NORMAL_BET_SIZE
		self.doubled_down = False

	def add_card(self, card):
		"""Adds a card to the players hand

		Parameters
		----------
		card:		Card()
					card to be added to players hand
		"""
		self.cur_hand[0].add_card(card)

	def hit(self, card, idx):
		"""Adds a card to the players hand

		Parameters
		----------
		card:		Card()
					card to be added to players hand
		idx:		int
					index of hand to hit
		"""
		self.cur_hand[idx].add_card(card)

	def stand(self, idx):
		"""Adds a card to the players hand

		Parameters
		----------
		idx:		int
					index of hand to stans
		"""
		self.cur_hand[idx].stand()

	def split(self):
		card1, card2 = self.cur_hand[0].split_cards()
		self.balance -= self.bet_size
		self.cur_hand = [Hand([card1]), Hand([card2])]

	def double_down(self):
		self.balance -= self.bet_size
		self.doubled_down = True

	def get_cur_hand_rating(self, idx):
		return self.cur_hand[idx].get_rating()
		
	def evaluate_count(self, dealer):
		count = dealer.get_count()
		cards_left = dealer.shoe.size()
		true_count = count // (cards_left // 52)

		if true_count >= 12:
			self.bet_size = 300
		elif true_count >= 2:
			self.bet_size = TRUE_COUNT_STRATEGY[true_count]
		else:
			self.bet_size = NORMAL_BET_SIZE

	def decision(self, dealer, hand, first):
		if first:
			if hand.is_paired():
				try:
					if hand.get_final_rating() == 2:
						return split(22, dealer.show_card_rating())
					return split(hand.get_final_rating(), dealer.show_card_rating())
				except:
					if hand.is_soft:
						return soft_double(hand.get_final_rating(), dealer.show_card_rating())
					else:
						return hard_double(hand.get_final_rating(), dealer.show_card_rating())
			else:
				if hand.is_soft:
					return soft_double(hand.get_final_rating(), dealer.show_card_rating())
				else:
					return hard_double(hand.get_final_rating(), dealer.show_card_rating())
		else:
			if hand.is_soft:
				return soft_hit(hand.get_final_rating(), dealer.show_card_rating())
			else:
				return hard_hit(hand.get_final_rating(), dealer.show_card_rating())


	def reset(self):
		for hand in self.cur_hand:
			hand.init()
		self.cur_hand = self.cur_hand[:1]
		self.doubled_down = False

