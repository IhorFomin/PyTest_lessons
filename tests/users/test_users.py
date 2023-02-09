from src.baseclasses.response import Response
from src.schemas.user import User

# SERVICE_URL = "https://gorest.co.in/public/v1/users"
# resp = requests.get(SERVICE_URL)
# print(resp.__getstate__())
# print(resp.url)


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)
    # print(calculate)
    # print(calculate(1, 1))


def test_another():
    assert 1==1
