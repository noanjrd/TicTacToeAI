from Game import Game

# le robot c est les o et le joueur les x

g = Game()
# g.playrandomly()
# g.printgame()

# for i in range(3):
# 	g.checkfilled()
# 	for j in range(3):
# 		g.fill(i, j, "x")


# g.fill(0, 0, "x")
# g.check_victory()
# g.printgame()
# g.checkfilled()

while (g.checkfilled() == -1):
	print("\n\n")
	g.printgame()
	print("\n")
	# print("It's your turn!")
	x = int(input("x : "))
	y = int(input("y : "))
	if (g.fill(x,y,"x") == -1):
		continue
	if (g.check_victory() == 1):
		break
	g.playrandomly()
	if (g.check_victory() == 1):
		break


g.printgame()