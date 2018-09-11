from alch import Alch
from create_database import Song as Bong

class Controller:
    print('opsa')


class Model:
    def __init__(self):
        self.session = Alch().sesh()
