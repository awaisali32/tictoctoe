import tkinter as tk
from tkinter import messagebox


class TicTacToeGame:
    def __init__(self, rows=3, cols=3):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "✓"
        self.board = [["" for _ in range(cols)] for _ in range(rows)]

        self.buttons = [[None] * cols for _ in range(rows)]
        self.create_board()

    def create_board(self):
        board_frame = tk.Frame(self.window)
        board_frame.pack(pady=20)

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.buttons[i][j] = tk.Button(
                    board_frame, text="", font=("Helvetica", 24),
                    width=6, height=2, command=lambda row=i, col=j: self.handle_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def handle_click(self, row, col):
        if self.board[row][col] == "" and not self.is_winner() and not self.is_tie():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.is_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "✓" else "✓"

    def is_winner(self):
        for i in range(len(self.board)):
            if all(self.board[i][j] == self.current_player for j in range(len(self.board[0]))):
                return True
        for j in range(len(self.board[0])):
            if all(self.board[i][j] == self.current_player for i in range(len(self.board))):
                return True
        if all(self.board[i][i] == self.current_player for i in range(len(self.board))) or \
           all(self.board[i][len(self.board) - i - 1] == self.current_player for i in range(len(self.board))):
            return True
        return False

    def is_tie(self):
        return all(self.board[i][j] != "" for i in range(len(self.board)) for j in range(len(self.board[0])))

    def reset_game(self):
        self.current_player = "✓"
        self.board = [["" for _ in range(len(self.board[0]))] for _ in range(len(self.board))]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.buttons[i][j].config(text="")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToeGame(rows=3, cols=3)
    game.run()
