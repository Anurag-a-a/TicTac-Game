import tkinter as tk
#Anurag Athwale 20012263

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Let's Play Tic-Tac-Toe")
        self.current_turn = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", font=("Times New Roman", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.button_clicked(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.master, text="Player X's chance", font=("Times New Roman", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(self.master, text="Restart", font=("Times New Roman", 16), command=self.restart_game, bg="blue", fg="white")
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def button_clicked(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_turn
            self.buttons[i][j].config(text=self.current_turn, state="disabled")

            if self.check_win():
                self.status_label.config(text=f"Player {self.current_turn} wins!")
                self.disable_buttons()
            elif self.check_draw():
                self.status_label.config(text="It's a draw!")
                self.disable_buttons()
            else:
                self.current_turn = "O" if self.current_turn == "X" else "X"
                self.status_label.config(text=f"Player {self.current_turn}'s turn")


    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True

        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")
    
    def restart_game(self):
        self.current_turn = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")
        self.status_label.config(text="Player X's chance")


root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()