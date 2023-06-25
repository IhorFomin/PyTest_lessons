import pytest


@pytest.fixture
def get_testing_scenarios(request):
    if request.param == 'scenario_1':
        return {"name": "John"}
    elif request.param == 'scenario_2':
        return {"name": "Ann"}
    else:
        return {"name": "Anton"}


@pytest.fixture
def get_magic_method(get_number):
    print(f"Polychili chislo {get_number}")
    def _wrapper(additional_number):
        return additional_number + get_number       
    return _wrapper