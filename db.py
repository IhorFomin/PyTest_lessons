# метод для создания сесии
from sqlalchemy.orm import sessionmaker
# метод для создания движка
from sqlalchemy import create_engine
# метод для создания моделей
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

from configuration import CONNECTION_ROW


Model = declarative_base(name='Model')

engine = create_engine(CONNECTION_ROW)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)
