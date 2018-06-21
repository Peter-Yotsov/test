from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from alch import Alch

Base = declarative_base()

association_table = Table('association',
                          Base.metadata,
                          Column('playlist_id',
                                 Integer,
                                 ForeignKey('playlist.id')),
                          Column('song_id',
                                 Integer,
                                 ForeignKey('song.id')))


class Song(Base):
    __tablename__ = "song"
    id = Column(Integer, primary_key=True)
    track = Column(String, default='Unknown')
    band = Column(String, default='Unknown')
    album = Column(String, default='Unknown')
    release = Column(String, default='Unknown')
    # length = calculate in model

    def __str__(self):
        return "{} - {}".format(self.band, self.track)

    def __repr__(self):
        return self.__str__()


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


engine = Alch('sqlite:///some.db').engi()
Base.metadata.create_all(engine)

session = Alch('sqlite:///some.db').sesh()
session.commit()
