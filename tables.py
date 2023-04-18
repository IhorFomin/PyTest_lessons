from sqlalchemy import Boolean, Column, Integer, String

from db import Model

class Films(Model):

    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    name_film = Column(String)
    date_film = Column(String)
    primier_film = Column(Boolean)


class ItemType(Model):

    __tablename__ = 'item_type'

    item_id = Column(Integer, primary_key=True)
    item_type = Column(String)
