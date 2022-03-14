from game import Game
from player import AdvantagePlayer
import matplotlib.pyplot as plt

plt.style.use("dark_background")


class Simulation:
	"""This class represents a simulation 

	Methods
	-------
	simulate()		simulates <iters> blackjack hands
	plot_balance()	plots the balance over time
	"""
	def __init__(self, iters, count = True):
		self.iters = iters
		self.player = AdvantagePlayer('Cezar')
		self.count = count
		self.game = Game([self.player], count, verbose = False,)


	def simulate(self):
		"""Simulates <self.iters> blackjack games"""
		x = []
		balance = []
		count = []
		for i in range(1, self.iters + 1):
			x.append(i)
			balance.append(self.player.balance)
			# count.append(self.game.dealer.get_count())
			self.game.play_round()

		self.plot_balance(x, balance)


	def plot_balance(self, x, balance):
		"""Plots the balance of the player over time

		Parameters
		---------
		x:			list
					list representing games played
		balance:	list
					list representing the players balance over time
		"""
		plt.plot(x, balance)
		plt.ylabel("Balance")
		plt.xlabel("Games Played")

		plt.title(f"Balance ({self.iters} games)\nBasic Strategy + Counting" if self.count else f"Balance ({self.iters} games)\nBasic Strategy")
		plt.tight_layout()
		plt.show()


	def plot_balance_with_count(self, x, balance, count):
		"""Plots the balance overlayed with the count
		
		Parameters
		---------
		x:			list
					list representing games played
		balance:	list
					list representing the players balance over time
		count:		list
					list representing the count ovet time
		"""
		fig, ax1 = plt.subplots()

		if balance[0] > balance[-1]:
			color = 'red'
		else:
			color = 'green'
		ax1.set_xlabel('Games')
		ax1.set_ylabel('Balance', color = color)
		ax1.plot(x, balance, color = color)
		ax1.tick_params(axis = 'y', labelcolor = color)

		ax2 = ax1.twinx()

		color = 'blue'
		ax2.set_ylabel('Count')
		ax2.plot(x, count, color = color)
		ax2.tick_params(axis='y', labelcolor = color)

		fig.tight_layout()
		plt.show()



if __name__ == '__main__':
	simulation = Simulation(1_000_000, count = True)
	simulation.simulate()