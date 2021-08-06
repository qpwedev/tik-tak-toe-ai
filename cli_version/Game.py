import os
from game_base.Board import Board
from game_base.Player import Player
from cli_version.CLI import CLI
import time

class Game:
    def __init__(self):
        self.actual_player = None # Displays the player who is currently playing
        self.game_loop() # Starts the game loop

    def player_turn_decition(self, board, player, cli):
        '''The player is given the opportunity to select a position, 
        and the correct input is checked. 
        Otherwise, a function is called that indicates what the problem is'''
        while True:
            print()
            choise = input(player.player_char + ' TURN. Enter a number 1-9 > ')
            if choise not in ('1','2','3','4','5','6','7','8','9'):
                cli.not_valid_symbol(self, board)
                continue
            choise = int(choise)-1
            if board.free_position(choise):
                return choise
            else:
                cli.not_valid_position(self, board)  

    def game_mode(self, cli):
        '''The player is given the opportunity to choose the game mode.
        Valid input is checked'''
        self.entry = ''
        while self.entry != 'p' and self.entry != 'c':
            cli.clean_termial()
            print('Please, select game mode:\nP - Player vs Player\nC - Player vs Computer')
            self.entry = input().strip().lower()
        if self.entry == 'p':
            return True
        if self.entry == 'c':
            return False        

    def restart(self, board, cli):
        '''The player is given the option to continue 
        or finish the game and the correct input is checked.'''
        board.clean_board()
        self.entry = ''
        while self.entry != 'n' and self.entry != 'y':
            cli.clean_termial()
            cli.play_again_message()
            self.entry = input().strip().lower()
        if self.entry == 'y':
            return True
        if self.entry == 'n':
            return False 

    def switch_player_turn(self, player1, player2):
        if self.actual_player == player1: self.actual_player = player2
        else: self.actual_player = player1 

    def game_loop(self):
        board = Board()
        cli = CLI()
        
        while True:
            cli.intro()
            cli.clean_termial()
            
            if self.game_mode(cli):
                player1 = Player(True,'X', 'O')
                player2 = Player(True,'O', 'X')
            else:
                player1 = Player(True,'X', 'O')
                player2 = Player(False,'O', 'X')
            
            cli.clean_termial()
            cli.display_board(board)

            self.actual_player = player1
            while True:
                choise = self.player_turn_decition(board, self.actual_player, cli)
                board.update_board(choise, self.actual_player.player_char)
                cli.clean_termial()
                cli.display_board(board)
                if board.control_game_win(self.actual_player.player_char):
                    cli.print_win_text(self.actual_player)
                    break

                if board.control_game_tie():
                    cli.print_tie_text()
                    break
            
                # HUMAN TURN
                if player2.human:
                    self.switch_player_turn(player1, player2)
                    cli.clean_termial()
                    cli.display_board(board)
                # AI TURN
                else:
                    choise = player2.ai_turn_decition(board, self)
                    board.update_board(choise, player2.player_char)
                    cli.clean_termial()
                    cli.display_board(board)

                    if board.control_game_win(player2.player_char):
                        cli.print_win_text(player2)
                        break

                    if board.control_game_tie():
                        cli.print_tie_text()
                        break

            time.sleep(1.5) # The program waits 1.5 seconds before clearing the field and asking for a restart
            
            if self.restart(board, cli):
                continue
            else:
                cli.clean_termial()
                break
            