import pytest
import requests

from configuration import SERVICE_URL

# функция выполняэться до теста
@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response