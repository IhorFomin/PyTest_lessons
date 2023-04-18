import requests
import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses

import tables


@pytest.mark.parametrize("status", Statuses.list())
def test_something_1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


# @pytest.mark.parametrize("balance_value", [
#     "100",
#     "0",
#     "-10",
#     "ddddd"
# ])
# def test_something(balance_value, get_player_generator):
#     print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_something_2(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)
    

@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_something_3(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization(loc).set_number(15).build()
        ).build()
    print(object_to_send)


def test_get_data_films(get_db_session):
    data = get_db_session.query(tables.Films).first()
    print(data.name_film)

def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.ItemType, (tables.ItemType.item_id == 3))


# def test_try_to_add_testdata(get_db_session, get_add_method):
#     new_item_type = {"item_type":"MY_NEW_TYPE"}
#     item = tables.ItemType(**new_item_type)
#     get_add_method(get_db_session, item)
#     print(item.item_id)

def test_try_to_add_testdata(get_db_session, get_add_method, get_item_type_generator):
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    print(item.item_id)


def test_try_to_add_testdata_gen(generate_item_type):
    print(generate_item_type.item_id)