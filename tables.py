from sqlalchemy import Boolean, Column, Integer, String

from db import Model

class Films(Model):

    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    name_film = Column(String)
    date_film = Column(String)
    primier_film = Column(Boolean)
