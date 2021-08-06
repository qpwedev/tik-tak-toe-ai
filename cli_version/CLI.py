import os

class CLI:
    def not_valid_symbol(self, game, board):
        self.clean_termial()
        self.display_board(board)
        print()
        print('## Not valid symbol ##')

    def not_valid_position(self, game, board):
        self.clean_termial()
        self.display_board(board)
        print()
        print('## Not empty position ##')  

    def clean_termial(self):
        '''Clearing the console.'''
        os.system('clear')

    def display_board(self, board):
        '''Printing a field (0-8) + printing an auxiliary field for the user.'''
        print(f' {board.board[0]} | {board.board[1]} | {board.board[2]}         1 | 2 | 3')
        print('———————————       ———————————')
        print(f' {board.board[3]} | {board.board[4]} | {board.board[5]}         4 | 5 | 6')
        print('———————————       ———————————')
        print(f' {board.board[6]} | {board.board[7]} | {board.board[8]}         7 | 8 | 9')

    def play_again_message(self):
        print('Do you want to play again? (Y/N)') 

    def print_win_text(self, player):
        print()
        print(player.player_char+' WON!!!\n')
    
    def print_tie_text(self):
        print()
        print('TIE!!!\n')

    def intro(self):
        self.entry = ''
        while self.entry != 'n' and self.entry != 'y':
            self.clean_termial()
            print('Welcome to the game\n')
            print('Do you want to read rules of the game? (Y/N)\n')
            self.entry = input().strip().lower()

        self.clean_termial()

        if self.entry == 'y':
            print('''1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n''') 

        self.entry = ''

        print('Lets start? (Press ENTER)')
        self.entry = input()
