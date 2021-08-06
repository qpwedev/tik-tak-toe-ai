import os
import pygame as pg
import sys
from gui_version.constants import *

class GUI:
    def __init__(self, WIDTH, HEIGHT):
        '''Pygame starts. 
        A window is created and a window name is assigned. 
        The background is filled with color'''
        pg.init()
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
        self.window.fill(BG_COLOR)
        pg.display.set_caption('Tik-Tak-Toe')

    def draw_lines_on_screen(self):
        # first horizontal
        pg.draw.line(self.window, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        # second horizontal
        pg.draw.line(self.window, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        # first vertical
        pg.draw.line(self.window, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # second vertical
        pg.draw.line(self.window, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


    def draw_actual_board_position(self, board):
        '''The array representing the playing field is checked. 
        Depending on the current position, drawing occurs on the screen'''
        for i in range(9):
            row, column = self.translation_cordinates_index(i)
            if board.board[i] == 'X':
                pg.draw.line(self.window, CROSS_COLOR, (column * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)	
                pg.draw.line(self.window, CROSS_COLOR, (column * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board.board[i] == 'O':
                pg.draw.circle(self.window, CIRCLE_COLOR, (int(column * SQUARE_SIZE + SQUARE_SIZE//2), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH)


    def translation_cordinates_index(self, index):
        '''Depending on the current position, drawing occurs on the screen'''
        if index == 0: return (0, 0)
        if index == 1: return (0, 1)
        if index == 2: return (0, 2)
        if index == 3: return (1, 0)
        if index == 4: return (1, 1)
        if index == 5: return (1, 2)
        if index == 6: return (2, 0)
        if index == 7: return (2, 1)
        if index == 8: return (2, 2)
        if index == (0, 0): return 0
        if index == (0, 1): return 1
        if index == (0, 2): return 2
        if index == (1, 0): return 3
        if index == (1, 1): return 4
        if index == (1, 2): return 5
        if index == (2, 0): return 6
        if index == (2, 1): return 7
        if index == (2, 2): return 8

    def draw_text(self, text, size, x, y, color):
        font = pg.font.SysFont(None, size)  
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.window.blit(text_surface,text_rect)

    def draw_main_menu(self):
        self.window.fill(BG_COLOR)
        pg.draw.rect(self.window, PURPLE, pg.Rect(0, 0, 300, 600))
        pg.draw.rect(self.window, PINK, pg.Rect(100, 80, 380, 70))
        self.draw_text('Welcome to tic-tac-toe', 50, 290, 100, MAIN_MENU_TEXT_COLOR)
        self.draw_text('Please, select the mode', 35, 290, 130, MAIN_MENU_TEXT_COLOR)
        self.draw_text('PvP', 80, 150, 300, MAIN_MENU_TEXT_COLOR)
        self.draw_text('PvC', 80, 450, 300, MAIN_MENU_TEXT_COLOR)
        pg.display.update()

    def draw_main_board(self):
        self.window.fill(BG_COLOR)
        self.draw_lines_on_screen()

    def mouse_click_position(self,event):
        '''The click position is tracked. 
        Next, the coordinates are converted to a format in which the first digit is the row number, 
        and the second is the column number.
        Then it is converted from this format to the format of the index number in the array'''
        mouse_positionx = event.pos[0]
        mouse_positiony = event.pos[1]
        column = (mouse_positionx // 200) 
        row = (mouse_positiony // 200)
        return self.translation_cordinates_index((row,column))

    def draw_win_text(self, actual_player):
        self.draw_text(f'{actual_player.player_char} WON!',40,305,20, WIN_TIE_RESTART)
        self.draw_text('press R to restart',40,300,580, WIN_TIE_RESTART)
    
    def draw_tie_text(self):
        self.draw_text('TIE!',40,305,20, WIN_TIE_RESTART)
        self.draw_text('press R to restart',40,300,580, WIN_TIE_RESTART)

    def window_update(self, board):
        self.draw_actual_board_position(board)
        pg.display.update()

    def music(self, category):
        '''Turn on different music depending on the situation.'''
        try:
            current_path = os.path.dirname(__file__) 
            if category == 'background':
                music_path = os.path.join(current_path + '/music/ElevatorMusic.mp3') 
                pg.mixer.music.load(music_path)
                pg.mixer.music.play(-1)
                pg.mixer.music.set_volume(0.05)

            elif category == 'lose':
                music_path = os.path.join(current_path + '/music/SadViolin.mp3') 
                pg.mixer.music.load(music_path)
                pg.mixer.music.play(1)
                pg.mixer.music.set_volume(0.05)

            elif category == 'win':
                music_path = os.path.join(current_path + '/music/Heavenly.mp3') 
                pg.mixer.music.load(music_path)
                pg.mixer.music.play(1)
                pg.mixer.music.set_volume(0.05)

            elif category == 'tie':
                music_path = os.path.join(current_path + '/music/Pizza.mp3') 
                pg.mixer.music.load(music_path)
                pg.mixer.music.play(1)
                pg.mixer.music.set_volume(0.05)

            elif category == 'turn':
                music_path = os.path.join(current_path + '/music/Click.mp3') 
                pg.mixer.Sound(music_path).play()

            elif category == 'stop':
                pg.mixer.music.stop()
        except:
            return
        