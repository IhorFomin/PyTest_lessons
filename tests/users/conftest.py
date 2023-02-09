import pytest
import requests

from configuration import SERVICE_URL

# функция выполняэться до теста
@pytest.fixture
def get_users():
    responce = requests.get(SERVICE_URL)
    return responce