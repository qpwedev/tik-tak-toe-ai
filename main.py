import os 

# Tik-tak-toe with AI and two versions of interface
# First year, winter 2020
# Programming 1

def main():
    choise = ''
    while choise != 'gui' and choise != 'cli':
        os.system('clear')
        print('Do you want to play GUI or CLI version? GUI/CLI')
        choise = input().strip().lower()
        if choise == 'gui':
            from gui_version.Game import Game
            break
        if choise == 'cli':
            from cli_version.Game import Game
            break
    game = Game()

main()
