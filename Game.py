import random


class Game:
    def __init__(self, level = 0):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.level = level

    def fill(self, x, y, player):
        """
        This function fills the selected case on the board.
        """
        x -= 1
        y -= 1
        if x < 0 or x >= 3 or y < 0 or y >= 3:
            return -1
        elif self.board[y][x] != " ":
            return -1
        else:
            self.board[y][x] = player
        return 1

    def check_victory(self, player, ai):
        """
        This function checks if a player has won the game.
        """
        for i in self.board:
            if i[0] == i[1] == i[2] and i[0] != " ":
                if i[0] == "o":
                    return ai
                else:
                    return player
        for i in range(3):
            if  self.board[0][i] == self.board[1][i] == self.board[2][i] \
            and self.board[0][i] != " " :
                if self.board[0][i] == "o":
                    return ai
                else:
                    return player
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] != " ") \
        		 or ( self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != " " ):
            if self.board[1][1] == "o":
                return ai
            else:
                return player
        return 0

    def check_filled(self) -> bool:
        """
        This function checks if the board is filled.
        """
        for i in self.board:
            if " " in i:
                return False
        return True

    def play_randomly(self):
        """
        This function, when the level chosen by the player is EASY, 
        places the AI's pawn randomly on the board.
        """
        if self.check_filled() == True:
            return -1
        while True:
            y = random.randint(0, 2)
            x = random.randint(0, 2)
            if self.board[y][x] == " ":
                self.board[y][x] = "o"
                return 1

    def minimax(self, player, depth):
        """
        This function recursively checks every case of the board up to 'depth' depth to help the 
        AI win the game.
        """
        if self.check_victory(1, 1) == 1 or self.check_filled() == True \
            or depth >= self.level :
            return self.check_victory(-1,1)
        if player == "o":
            bestscore = float("-inf")
        if player == "x":
            bestscore = float("+inf")
        for j in range(3):
            for i in range(3):
                if self.board[j][i] == " ":
                    self.board[j][i] = player
                    if player == "o":
                        score = self.minimax("x", depth + 1)
                    else:
                        score = self.minimax("o", depth + 1)
                    self.board[j][i] = " "
                    if player == "o":
                        bestscore = max(bestscore, score)
                    else:
                        bestscore = min(bestscore, score)
        return bestscore

    def AI_move(self):
        """
        This function chooses the best case to be played for the AI
        """
        bestscore = float("-inf")
        bestcase = [0, 0]
        if self.level == 0:
            self.play_randomly()
            return
        for j in range(3):
            for i in range(3):
                if self.board[j][i] == " ":
                    self.board[j][i] = "o"
                    score = self.minimax("x", 0)
                    self.board[j][i] = " "
                    if score > bestscore:
                        bestscore = score
                        bestcase[0] = j
                        bestcase[1] = i
        self.board[bestcase[0]][bestcase[1]] = "o"
