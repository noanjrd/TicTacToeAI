from Game import Game

g = Game()

while True:
	print("Choose the AI's level:\n- (1) Easy\n- (2) Inter\n- (3) Impossible")
	lvl = input("type here : ")
	if lvl == "Easy" or lvl == "1" or lvl == "easy":
		g.level = 0
		break
	if "Inter" in lvl or "2" in lvl or "inter" in lvl:
		g.level=1
		break
	if "impossible" in lvl or "3" in lvl or "Impossible" in lvl:
		g.level=100
		break

while True:
	print("\n\n")
	g.printgame()
	print("\n")
	if (g.checkfilled() == 1):
		print("No one won!")
		break
	x = int(input("x : "))
	y = int(input("y : "))
	if (g.fill(x,y,"x") == -1):
		continue
	if (g.check_victory() == 1):
		break
	g.AI_move()
	if (g.check_victory() == 1):
		break

exit(0)

