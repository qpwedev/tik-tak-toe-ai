class Board:
    def __init__(self):
        '''Structure of the playing field as a list.'''
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']

    def update_board(self, position, player):
        '''Сhecking the field cell to be empty. 
        Сhanging the field on this index by the player symbol'''
        if self.board[position] == '-':
            self.board[position] = player

    def control_game_win(self, player_char):
        '''Checking winning combinations on this field.
        # gorizontal 1-3
        # vertical 4-6
        # diagonals 7-8'''
        return (self.board[0] == player_char and self.board[0] == self.board[1] ==  self.board[2]) \
        or (self.board[3] == player_char and self.board[3] == self.board[4] ==  self.board[5]) \
        or (self.board[6] == player_char and self.board[6] == self.board[7] ==  self.board[8]) \
        or (self.board[0] == player_char and self.board[0] == self.board[3] ==  self.board[6]) \
        or (self.board[1] == player_char and self.board[1] == self.board[4] ==  self.board[7]) \
        or (self.board[2] == player_char and self.board[2] == self.board[5] ==  self.board[8]) \
        or (self.board[0] == player_char and self.board[0] == self.board[4] ==  self.board[8]) \
        or (self.board[2] == player_char and self.board[2] == self.board[4] ==  self.board[6]) \

    def control_game_tie(self):
        '''Сhecking if each cell of the field is different from-return the True.'''
        for i in self.board:
            if i == '-': return False
        return True

    def free_position(self, position):
        '''Сhecking if the position is free (- character).'''
        return self.board[position] == '-'

    def clean_board(self):
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']