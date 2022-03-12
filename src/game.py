
from dealer import Dealer
from player import AdvantagePlayer
import os

players = [AdvantagePlayer('Cezar')]


class Game:

	def __init__(self, players, count, verbose = False):
		self.games = 1
		self.players = players
		self.verbose = verbose
		self.count = count
		self.dealer = Dealer(players)


	def _init(self):
		new_players = []
		for player in self.players:
			player.reset()
			new_players.append(player)
		self.players = new_players
		self.dealer.reset()

	def play_round(self):
		if self.verbose:
			os.system('cls' if os.name == 'nt' else 'clear')

		self._init()
		self.cur_players = self.players.copy()
		self.take_bets()
		self.dealer.deal()
		if self.verbose:
			self.display(stood = True)
		self.check_blackjack()
		self.decision(first = True)


		while True:
			if self.check_winners():
				break
			if self.verbose:	
				self.display(not self.all_players_stand())
			self.decision()

		if self.count:

			for player in self.cur_players:
				player.evaluate_count(self.dealer)
		self.games += 1


	def take_bets(self):
		for player in self.cur_players:
			player.balance -= player.bet_size



	def check_blackjack(self):
		for player in self.cur_players:
			for hand in player.cur_hand:
				if hand.blackjack:
					player.balance += player.bet_size * 2.5
					self.cur_players.remove(player)


	def check_winners(self):
		for player in self.cur_players:
			for hand in player.cur_hand:
				
				if not hand.bust and not hand.blackjack and not hand.stood and not player.doubled_down:
					return False
		return self.eval_winners()


	def eval_winners(self):
		self.dealer.hit()
		if self.verbose:
			self.display()

		dealer_score = self.dealer.final_rating()


		for player in self.cur_players:
			for hand in player.cur_hand:
				player_score = hand.get_final_rating()
				if player_score <= 21:
					if dealer_score > 21 or player_score > dealer_score:
						if player.doubled_down:
							player.balance += player.bet_size * 2
						player.balance += player.bet_size * 2
						if self.verbose:
							print(f'{player.name} wins!')
					elif dealer_score > player_score:
						if self.verbose:
							print('Dealer wins!')
					else:
						if self.verbose:
							print('Push!')
						player.balance += player.bet_size 

				else:
					if self.verbose:
						print('Bust!')

		if self.verbose:
			print('-------------------------------\n\n')

		return True



	def all_players_stand(self):
		for player in self.cur_players:
			for hand in player.cur_hand:
				if not hand.stood:
					return False
		return True



	def display(self, stood = False):
		if stood:
			print(f'\n\nDealer: {self.dealer.get_cur_hand_display(stood)}\n')
		else:
			print(f'\n\nDealer: {self.dealer.get_cur_hand_display()} {self.dealer.get_cur_hand_rating_display()}\n')

		for player in self.cur_players:
			for idx, hand in enumerate(player.cur_hand):
				print(f'{player.name}: {hand} ({player.get_cur_hand_rating(idx)}) - ${player.balance}')

		print(f"\nCount: {self.dealer.get_count()}\n")


	def decision(self, first = False):
		for player in self.cur_players:
			for idx, hand in enumerate(player.cur_hand):

				if not hand.blackjack and not hand.bust and not hand.stood and not player.doubled_down:
					decision = player.decision(self.dealer, hand, first)
					# decision = int(input())
					if decision == 0:
						if self.verbose:
							print('Hit!')
						card = self.dealer.pop_card()
						player.hit(card, idx)
					if decision == 1:
						if self.verbose:
							print('Stand!')
						player.stand(idx)
					if decision == 2:
						if self.verbose:
							print('Split!')
						player.split()

						card = self.dealer.pop_card()
						player.hit(card, 0)
					if decision == 3:
						if self.verbose:
							print('Double Down!')
						card = self.dealer.pop_card()
						player.double_down()
						player.hit(card, idx)




if __name__ == '__main__':



	players = [AdvantagePlayer('Cezar')]
	game = Game(players, verbose = True)
	play_again = 1
	while play_again == 1:

		game.play_round()
		play_again = int(input("Play again? Y[1]N[0]\n"))
		


