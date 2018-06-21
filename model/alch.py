from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Alch:
    def __init__(self, playlist_name):
        self.database = playlist_name

    def engi(self):
        engine = create_engine(self.database)
        return engine

    def sesh(self):
        Session = sessionmaker(bind=self.engi)
        session = Session()
        return session
