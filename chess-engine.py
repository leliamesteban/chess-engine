class ChessEngine:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        return board

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def get_legal_moves(self, color):
        # Implement logic to generate legal moves for the given color
        return []

    def make_move(self, move):
        r1, c1, r2, c2 = move
        self.board[r2][c2] = self.board[r1][c1]
        self.board[r1][c1] = ' '

    def evaluate_board(self):
        # Implement a simple evaluation function
        return 0

    def minimax(self, depth, maximizing_player):
        if depth == 0:
            return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_legal_moves("white"):
                self.make_move(move)
                eval = self.minimax(depth - 1, False)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_legal_moves("black"):
                self.make_move(move)
                eval = self.minimax(depth - 1, True)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
            return min_eval

    def undo_move(self, move):
        r2, c2, r1, c1 = move
        self.board[r1][c1] = self.board[r2][c2]
        self.board[r2][c2] = ' '

    def parse_move(self, move_str):
        # Converts a move from standard notation (e.g., 'e2e4') to tuple form (e.g., (6, 4, 4, 4))
        files = 'abcdefgh'
        r1 = 8 - int(move_str[1])
        c1 = files.index(move_str[0])
        r2 = 8 - int(move_str[3])
        c2 = files.index(move_str[2])
        return (r1, c1, r2, c2)

    def cli_play(self):
        self.print_board()
        while True:
            user_move = input("Enter your move (e.g., e2e4): ")
            if user_move.lower() == 'exit':
                break
            move = self.parse_move(user_move)
            self.make_move(move)
            self.print_board()
            print("Engine thinking...")
            best_move = self.minimax(3, False)  # Change depth as needed
            self.make_move(best_move)
            self.print_board()

if __name__ == "__main__":
    engine = ChessEngine()
    engine.cli_play()
