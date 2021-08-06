from game_base.Board import Board

class Player:
    def __init__(self, human, player_char, player_opposite_char):
        self.human = human # True if it is a human else False
        self.player_char = player_char # Displays the symbol that the player is playing with (X/O)
        self.player_opposite_char = player_opposite_char # Displays the character that is played by the opposite player (X/O)

    def minmax(self, newboard, is_ai_turn):
        if newboard.control_game_win(self.player_char):
            return 1
        if newboard.control_game_win(self.player_opposite_char):
            return -1
        if newboard.control_game_tie():
            return 0

        if is_ai_turn:
            best_score = - float('inf')
            for i in range(9):
                if newboard.board[i] == '-':
                    newboard.board[i] = self.player_char
                    score = self.minmax(newboard, False)
                    newboard.board[i] = '-'
                    best_score = max(best_score, score)
        else:            
            best_score = float('inf')
            for i in range(9):
                if newboard.board[i] == '-':
                    newboard.board[i] = self.player_opposite_char
                    score = self.minmax(newboard, True)
                    newboard.board[i] = '-'
                    best_score = min(best_score, score)
        return best_score

    def ai_turn_decition(self, board, game):
        move = None
        best_score = -float('inf')
        newboard = Board()
        newboard.board = board.board[:]
        for i in range(9):
            if newboard.board[i] == '-':
                newboard.board[i] = self.player_char
                if newboard.control_game_win(self.player_char):
                    return i
                score = self.minmax(newboard, False)
                newboard.board[i] = '-'
                if score > best_score:
                    best_score = score
                    move = i
        return move
