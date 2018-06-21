from .controller import controllers
import sys

controllers.Controller()


class Menu:
    print('Welcome to Music Player')

    def start_up(self):
        choice = input('Would you like to [create] a new playlist \
or [load] an existing one?\n>>>')

        self.playlist_decision(choice)

    def playlist_decision(self, choice):
        if choice == 'create':
            print(choice)

        elif choice == 'load':
            print(choice, choice)

        elif choice == 'exit':
            sys.exit()

        else:
            choice = input('Please select a valid \
playlist option! [load/create]\n>>>')
            self.playlist_decision(choice)


# PLACE IN music_player.py
Menu().start_up()
