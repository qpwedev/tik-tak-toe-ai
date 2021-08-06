import pygame as pg
import sys
from gui_version.constants import *
from game_base.Player import Player
from gui_version.GUI import GUI
from game_base.Board import Board

class Game:
    def __init__(self):
        self.game_over = False # Displays whether the game is over or not
        self.actual_player = None # Displays the player who is currently playing
        self.game_loop() # Starts the game loop

    def mode_selection(self, player2):
        '''Player's choice of game mode. 
        If the click occurred on the left side of the screen, 
        the player2.human attribute becomes True, otherwise False'''
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_positionx = (event.pos[0])//300
                    if mouse_positionx == 1:
                        player2.human = False
                        return 
                    if mouse_positionx == 0:
                        player2.human = True
                        return


    def game_restart(self, board, gui, player1, player2):
        '''The Board is cleared and the move goes to the first player. 
        The game cycle starts and the main menu is drawn. Mode selection is offered'''
        board.clean_board()
        self.actual_player = player1
        self.game_over = False
        gui.draw_main_menu()
        self.mode_selection(player2)

    def switch_player_turn(self, player1, player2):
        if self.actual_player == player1: self.actual_player = player2
        else: self.actual_player = player1    

    def game_loop(self):
        board = Board()
        gui = GUI(WIDTH, HEIGHT)
        player1 = Player(True,'X', 'O')
        player2 = Player(True,'O', 'X')

        gui.draw_main_menu()
        self.mode_selection(player2)
        self.actual_player = player1

        gui.music('background')
        gui.draw_main_board()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        gui.music('stop')
                        self.game_restart(board, gui, player1, player2)
                        gui.music('background')
                        gui.draw_main_board()
                        
                if event.type == pg.MOUSEBUTTONDOWN and not self.game_over:
                    choise = gui.mouse_click_position(event)
                    
                    if not board.free_position(choise):
                        continue
                    
                    gui.music('turn')
                    board.update_board(choise, self.actual_player.player_char)

                    if board.control_game_win(self.actual_player.player_char):
                        gui.music('win')
                        gui.draw_win_text(self.actual_player)
                        self.game_over = True
                        break

                    if board.control_game_tie():
                        gui.music('tie')
                        gui.draw_tie_text()
                        self.game_over = True
                        break
                    
                    # HUMAN TURN
                    if player2.human:
                        self.switch_player_turn(player1, player2)
                        
                    # AI TURN
                    else:
                        choise = player2.ai_turn_decition(board, self)

                        board.update_board(choise, player2.player_char)
                        
                        if board.control_game_win(player2.player_char):
                            gui.music('lose')
                            gui.draw_win_text(player2)
                            self.game_over = True
                            break

                        if board.control_game_tie():
                            gui.music('tie')
                            gui.draw_tie_text()
                            self.game_over = True
                            break
                
                gui.window_update(board)
