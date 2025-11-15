import random

class Game:
	def __init__(self):
		self.tab = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

	def printgame(self):
		print("    1   2   3")
		print("   -----------")
		for i in range(3):
			print(f"{i + 1} |", end ="")
			for j in range(3):
				print(f" {self.tab[i][j]} ", end ="")
				if (j != 2):
					print("|", end ="")
			print("|")
			print("   -----------")

	def fill(self, x, y, c):
		x -=1
		y-=1
		if (x < 0 or x >= 3 or y < 0 or y >= 3):
			print("Not a possible case")
			return -1
		elif (self.tab[y][x] != " "):
			print("This is case has already been played")
			return -1
		else:
			self.tab[y][x] = c

	def check_victory(self):
		for i in self.tab:
			if i[0] == i[1] and i[0] == i[2] and i[0] != " ":
				if (i[0] == "o"):
					print("You lost :(")
				else:
					print("You won!")
				return 1
		for i in range(3):
			if (self.tab[0][i] == self.tab[1][i] and self.tab[0][i] == self.tab[2][i] and self.tab[0][i] != " "):
				if (self.tab[0][i] == "o"):
					print("You lost :(")
				else:
					print("You won!")
				return 1
		if ((self.tab[0][0] == self.tab[1][1] and self.tab[0][0] == self.tab[2][2] and self.tab[1][1] != " ") 
			or (self.tab[0][2] == self.tab[1][1] and self.tab[0][2] == self.tab[2][0] and self.tab[1][1] != " ")):
			if (self.tab[1][1] == "o"):
				print("You lost :(")
			else:
				print("You won!")
			return 1
		return -1

	def checkfilled(self):
		for i in self.tab:
			if " " in i:
				return -1
		return 1

	def playrandomly(self):
		if (self.checkfilled() == 1):
			return -1
		while True:
			y = random.randint(0,2)
			x = random.randint(0,2)
			if (self.tab[y][x] == " "):
				self.tab[y][x] = "o"
				return 1



