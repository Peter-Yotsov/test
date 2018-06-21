from alch import Alch


class Model:
    def __init__(self):
        self.session = Alch().sesh()
