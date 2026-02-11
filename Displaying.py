def print_game(board) -> None:
	print("    1   2   3")
	print("   -----------")
	for i in range(3):
		print(f"{i + 1} |", end ="")
		for j in range(3):
			print(f" {board[i][j]} ", end ="")
			if (j != 2):
				print("|", end ="")
		print("|")
		print("   -----------")
  
def check_winner(score, board) -> bool:
	if score == 0:
		return False
	print("\n")
	print_game(board)
	if score == 1:
		print("\nYou won!")
	else:
		print("\nYou lost :(")
	return True
