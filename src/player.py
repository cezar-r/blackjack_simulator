
from hand import Hand
from strategy import *

class AdvantagePlayer:

	def __init__(self, name, balance = 10_000):
		self.name = name
		self.cur_hand = [Hand()]
		self.balance = balance
		self.bet_size = 10
		self.doubled_down = False

	def add_card(self, card):
		self.cur_hand[0].add_card(card)

	def hit(self, card, idx):
		self.cur_hand[idx].add_card(card)

	def stand(self, idx):
		self.cur_hand[idx].stand()

	def split(self):
		card1, card2 = self.cur_hand[0].split_cards()
		self.cur_hand = [Hand([card1]), Hand([card2])]


	def double_down(self):
		self.doubled_down = True


	def get_cur_hand_rating(self, idx):
		return self.cur_hand[idx].get_rating()
		

	def evaluate_count(self):
		pass


	def decision(self, dealer, hand, first):
		if first:
			if hand.is_paired():
				try:
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
				return hard_double(hand.get_final_rating(), dealer.show_card_rating())


	def reset(self):
		for hand in self.cur_hand:
			hand.init()

