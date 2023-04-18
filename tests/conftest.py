import pytest

from random import randrange
from src.generators.player import Player
from src.generators.item_type_generator import ItemsTypeBuilder

from db import Session
import tables


@pytest.fixture
def get_item_type_generator():
    return ItemsTypeBuilder()


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    # print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number
    # print(f"Number at home {number}")


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_method(session, item):
    session.add(item)
    session.commit()


@pytest.fixture
def get_delete_method():
    return delete_test_data


@pytest.fixture
def get_add_method():
    return add_method


@pytest.fixture
def generate_item_type(get_db_session, get_item_type_generator, get_add_method, get_delete_method):
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    yield item
    get_delete_method(get_db_session, tables.ItemType, (tables.ItemType.item_id == item.item_id))