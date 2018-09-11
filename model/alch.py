from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Playlist(Base):
    __tablename__ = "playlist"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    songs = relationship('Song',
                         secondary=association_table)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


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
