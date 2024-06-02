class Grid:
    def __init__(self):
        self.grid = [[None for _ in range(6)] for _ in range(7)]

    def placeCoin(self, col, coin):

        if col < 0 or col > 6:
            #print("Invalid row")
            return False

        if coin not in ("red", "yellow"):
            print("Invalid color")
            return False

        for row in range(5, -1, -1):
            if self.grid[col][row] is None:
                self.grid[col][row] = coin
                #print(f" {coin} Coin placed at {col}, {row}")
                return True

        print("no available place")
        return False

    def verifyWinHorizontal(self):

        for row in range(5, -1, -1):
            for col in range(4):
                if self.grid[col][row] == "yellow" and self.grid[col + 1][row] == "yellow" \
                        and self.grid[col + 2][row] == "yellow" and self.grid[col + 3][row] == "yellow":
                    print("Yellow wins with horizontal")
                    return True
                if self.grid[col][row] == "red" and self.grid[col + 1][row] == "red" \
                        and self.grid[col + 2][row] == "red" and self.grid[col + 3][row] == "red":
                    print("Red wins with horizontal")
                    return True
        #print("Nobody wins with horizontal")
        return False

    def verifyWinVertical(self):
        for row in range(5, -1, -1):
            for col in range(7):
                if self.grid[col][row] == "yellow" and self.grid[col][row - 1] == "yellow" \
                        and self.grid[col][row - 2] == "yellow" and self.grid[col][row - 3] == "yellow":
                    print("Yellow wins with vertical")
                    return True
                if self.grid[col][row] == "red" and self.grid[col][row - 1] == "red" \
                        and self.grid[col][row - 2] == "red" and self.grid[col][row - 3] == "red":
                    print("Red wins with vertical")
                    return True
        #print("Nobody wins with vertical")
        return False

    def verifyWinDiagonal(self):

        for row in range(2, -1, -1):
            for col in range(4):

                if self.grid[col][row] == "yellow" and self.grid[col + 1][row + 1] == "yellow" \
                        and self.grid[col + 2][row + 2] == "yellow" and self.grid[col + 3][row + 3] == "yellow":
                    print("Yellow wins with diagonal")
                    return True

                if self.grid[col][row] == "red" and self.grid[col + 1][row + 1] == "red" \
                        and self.grid[col + 2][row + 2] == "red" and self.grid[col + 3][row + 3] == "red":
                    print("Red wins with diagonal")
                    return True

        for row in range(5, 2, -1):
            for col in range(4):

                if self.grid[col][row] == "yellow" and self.grid[col + 1][row - 1] == "yellow" \
                        and self.grid[col + 2][row - 2] == "yellow" and self.grid[col + 3][row - 3] == "yellow":
                    print("Yellow wins with diagonal")
                    return True

                if self.grid[col][row] == "red" and self.grid[col + 1][row - 1] == "red" \
                        and self.grid[col + 2][row - 2] == "red" and self.grid[col + 3][row - 3] == "red":
                    print("Red wins with diagonal")
                    return True

        #print("Nobody wins with diagonal")
        return False

    def verifyAllWins(self):
        if self.verifyWinHorizontal() or self.verifyWinVertical() or self.verifyWinDiagonal():
            return True
        else:
            return False

    def gridFilled(self):
        for row in range(6):
            for col in range(7):
                if self.grid[col][row] is None:
                    return False
        return True

    def verifyDraw(self):
        if not self.verifyWinHorizontal() and not self.verifyWinVertical() \
                and not self.verifyWinDiagonal() and self.gridFilled():
            print("Draw")
            return True
        return False


class Game:
    def __init__(self, colorPlayer1, colorPlayer2):
        if colorPlayer1 not in ("yellow", "red"):
            raise ValueError("colorPlayer1 must be 'yellow' or 'red'")

        if colorPlayer2 not in ("yellow", "red"):
            raise ValueError("colorPlayer1 must be 'yellow' or 'red'")

        if colorPlayer1 == colorPlayer2:
            raise ValueError("players must be different colors")

        self.gaming = Grid()
        self.player1 = colorPlayer1
        self.player2 = colorPlayer2

    def seeSomething(self):

        for row in range(0, 15, 1):
            print("_", end="")
        print("\n", end="")

        for row in range(6):
            for col in range(7):
                #print(row, col)
                if self.gaming.grid[col][row] is None:
                    print("| ", end="")
                if self.gaming.grid[col][row] == "red":
                    print("|R", end="")
                if self.gaming.grid[col][row] == "yellow":
                    print("|Y", end="")
            print("|\n", end="")

        for col in range(15):
            print("-", end="")
        print("\n", end="")

    def gamingTime(self):
        while not self.gaming.verifyDraw():

            self.seeSomething()
            print(f" Player 1 {self.player1} turn")
            while True:
                player1Move = input("Choose a column from 0 to 6: ")
                if self.gaming.placeCoin(int(player1Move), self.player1):
                    break
                else:
                    print("Invalid move. Please choose another column.")

            #self.gaming.placeCoin(int(player1Move), self.player1)

            self.seeSomething()

            if self.gaming.verifyAllWins():
                print(f"{self.player1} wins!")
                break

            print(f" Player 2 {self.player2} turn")
            while True:
                player2Move = input("Choose a column from 0 to 6: ")
                if self.gaming.placeCoin(int(player2Move), self.player2):
                    break
                else:
                    print("Invalid move. Please choose another column.")

            self.seeSomething()

            if self.gaming.verifyAllWins():
                print(f"{self.player2} wins!")
                break