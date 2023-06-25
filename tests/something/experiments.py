import pytest


class Letter:

    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

    def __str__(self) -> str:
        return f"Letter {self.letter}, Position {self.position}"
    

def get_cases():
    return [
        Letter("a", 1),
        Letter("b", 2)
    ]


@pytest.mark.parametrize("my_value", get_cases(), ids=str)
def test_my_magic_method(my_value):
    print(my_value)


@pytest.mark.parametrize("get_testing_scenarios", ['scenario_1'], indirect=True)
def test_data_indirect(get_testing_scenarios):
    print(get_testing_scenarios)


def test_magic_method(get_magic_method):
    print(get_magic_method(1))


def test_option(getting_env):
    print(getting_env)
