class Game:
    gameover = None
    positions: dict[int, str] = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }
    marked_positions = []
    user_a: str
    user_b: str

    def __init__(self):
        print("Welcome to Tic Tac Toe game!")

        self.user_a = input("choose your mark 'O' or 'X'? ").upper()
        self.user_b = "O" if self.user_a == "X" else "X"
        print(f"\nuserA = {self.user_a}; userB = {self.user_b}")

    def print_board(self):
        print(
            f"""
              {self.positions[7]}| {self.positions[8]} |{self.positions[9]}
            ---|---|---
              {self.positions[4]}| {self.positions[5]} |{self.positions[6]}
            ---|---|---
              {self.positions[1]}| {self.positions[2]} |{self.positions[3]}
            """
        )

    def update_position(self, pos: int, sign: str):
        self.positions[pos] = sign
        self.marked_positions.append(pos)
        self.print_board()

    def check_gameover(self, value: str):
        if self.positions[1] == self.positions[2] == self.positions[3]:
            self.gameover = value

        elif self.positions[4] == self.positions[5] == self.positions[6]:
            self.gameover = value

        elif self.positions[7] == self.positions[8] == self.positions[9]:
            self.gameover = value

        elif self.positions[1] == self.positions[4] == self.positions[7]:
            self.gameover = value

        elif self.positions[2] == self.positions[5] == self.positions[8]:
            self.gameover = value

        elif self.positions[3] == self.positions[6] == self.positions[9]:
            self.gameover = value

        elif self.positions[1] == self.positions[5] == self.positions[9]:
            self.gameover = value

        elif self.positions[7] == self.positions[5] == self.positions[3]:
            self.gameover = value

    def start(self):
        print("\nStarting the game...")

        while not self.gameover:
            self.print_board()

            turn_a = int(
                input(f"\nuserA's({self.user_a}) turn, input position number: ")
            )
            self.update_position(turn_a, self.user_a)
            self.check_gameover(self.user_a)

            if self.gameover:
                break

            turn_b = int(
                input(f"\nuserB's({self.user_b}) turn, input position number: ")
            )
            self.update_position(turn_b, self.user_b)
            self.check_gameover(self.user_b)

        if self.gameover == "X":
            print(f"UserA({self.user_a}) wins")
        else:
            print(f"UserB({self.user_b}) wins")


Game().start()
