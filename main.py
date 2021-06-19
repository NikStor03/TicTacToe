# tic tac toe by NikStor#3003
import os
import errors

"""
    Tic Tac Toe By NikStor
    My Discord: 🍀 NikStor 🌿#3003
"""


class TicTacToe:

    def __init__(self):
        self.grid = [["-", "-", '-'],
                    ['-', '-', '-'],
                    ['-', '-', '-']]

    # Main logic
    def logic(self, x: int, y: int, symbol: str) -> bool:
        if self.grid[y][x] != "-":
            raise errors.CellAlreadyTaken("({x}, {y}) cell is already taken".format(x=x, y=y))

        self.grid[y][x] = symbol

        # row and column check
        amount_x = 0
        amount_y = 0
        for row in self.grid[y]:
            if row == symbol:
                amount_x += 1

        for col in self.grid:
            if col[x] == symbol:
                amount_y += 1

        # obliquely check
        original = [symbol, symbol, symbol]

        first_check = []
        for i in range(3):
            first_check.append(self.grid[i][i])

        second_check = []
        j = 2
        for i in range(3):
            second_check.append(self.grid[i][j])
            j -= 1

        # Return who won
        if (amount_x == 3 or amount_y == 3) or (second_check == original or first_check == original):
            return True

    def draw(self) -> str:

        row = "   0   1   2 \n  ───────────\n"
        for i in range(3):
            for j in range(3):
                if j == 0:
                    row += '{num}| {cell} |'.format(num=i, cell=self.grid[i][j])
                else:
                    row += ' {cell} |'.format(num=i, cell=self.grid[i][j])
            row += "\n"
        return row

    def game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
            ╭---╮   \\    /  |    /| _______  |  /
            |   |    \\  /   |   / |    |     | /
            |---╯     \\/    |  /  |    |     |/
            |---╮      |    | /   |    |     |\\
            |---╯      |    |/    | ───┴───  | \\
            """)
        print("Rules: In field you should write coordinates by (x y).\nExample: 0 1\n\n\n")
        game_over = False
        current_move = 1
        while not game_over:

            try:
                print(self.draw())

                if current_move == 1:
                    step = input("First player: ")
                    won = self.logic(int(step.split()[0]), int(step.split()[1]), "x")
                else:
                    step = input("Second player: ")
                    won = self.logic(int(step.split()[0]), int(step.split()[1]), "o")

            except errors.CellAlreadyTaken:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("This cell was already taken!")

            except IndexError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid coordinate")

            else:
                os.system('cls' if os.name == 'nt' else 'clear')

                if won:
                    print(self.draw())
                    if current_move == 1:
                        print("X - winner!")
                    else:
                        print("O - winner!")
                    game_over = True

                if current_move == 2:
                    current_move -= 1
                else:
                    current_move += 1