from game import Game
import displaying

def get_ai_level():
	while True:
		print("Choose the AI's level:\n- (1) Easy\n- (2) Inter\n- (3) Impossible")
		lvl = input("Type here : ").lower()
		if lvl in ["1", "easy"]:
			return 0
		if "inter" in lvl or "2" in lvl:
			return 1
		if "impossible" in lvl or "3" in lvl:
			return 100
		print("\nInvalid input, please try again.")

def play_game():
	try : 
		g = Game(get_ai_level())

		while True:
			print("\n")
			displaying.print_game(g.board)
			
			if g.check_filled():
				print("No one won (Draw)!")
				break

			if not player_turn(g):
				continue
				
			if displaying.check_winner(g.check_victory(1, -1), g.board):
				break

			g.AI_move()
			
			if displaying.check_winner(g.check_victory(1, -1), g.board):
				break
	except KeyboardInterrupt:
		print("\nGame interrupted by user. Goodbye!")

def player_turn(game):
	try:
		x = int(input("x (1-3): "))
		y = int(input("y (1-3): "))
		if game.fill(x, y, "x") == -1:
			print("\nNot a possible case")
			return False
		return True
	except ValueError:
		print("\nWrong input: please enter numbers.")
		return False

if __name__ == "__main__":
	play_game()