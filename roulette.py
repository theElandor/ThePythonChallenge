import random
import pygal

##on even the player is going to win 
##on odd the roulette is going to win

class Roulette():
	def __init__(self):
		self.numbers = []
		self.winned = 0 ##player wins
		self.lost = 0  ##player losts
	def fill(self):
		for i in range(0,37):
			self.numbers.append(i)
	def play_games(self,num):
		for i in range(0,num):
			n = random.randint(0,36)
			if n == 0 or n%2 != 0:
				self.lost += 1
			else:
				self.winned += 1
	def show(self):
		print("player winned games: "+str(self.winned))
		print("player lost games: "+str(self.lost))
	def plot(self):
		table = pygal.Bar()
		table.title="Roulette results."
		res = []
		res.append(self.winned)
		res.append(self.lost)
		table.x_labels = ['Winned','Lost']
		table.add('games',res)
		table.render_to_file('roulette_results.svg')

roulette = Roulette()
roulette.fill()
games = int(input("Inserire il numero di partite--> "))
roulette.play_games(games)
roulette.show()
roulette.plot()


