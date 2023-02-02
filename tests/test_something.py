import requests

from src.baseclasses.response import Response
from src.schemas.user import User

# SERVICE_URL = "https://gorest.co.in/public/v1/users"
# resp = requests.get(SERVICE_URL)
# print(resp.__getstate__())
# print(resp.url)


def test_getting_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)


def test_another():
    assert 1==1


# z = {
#     'meta': {
#         'pagination': {
#             'total': 2276,
#             'pages': 228,
#             'page': 1,
#             'limit': 10,
#             'links': {
#                 'previous': None,
#                 'current': 'https://gorest.co.in/public/v1/users?page=1',
#                 'next': 'https://gorest.co.in/public/v1/users?page=2'
#             }
#         }
#     },
#     'data': [{
#         'id': 3046,
#         'name': 'Chandramauli Khatri DC',
#         'email': 'chandramauli_khatri_dc@kertzmann.net',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 3044,
#         'name': 'Dron Iyer',
#         'email': 'iyer_dron@bruen.org',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 3043,
#         'name': 'Rageshwari Dubashi',
#         'email': 'rageshwari_dubashi@prohaska-osinski.co',
#         'gender': 'male',
#         'status': 'active'
#     }, {
#         'id': 3041,
#         'name': 'Brahmaanand Pillai',
#         'email': 'brahmaanand_pillai@nolan-flatley.com',
#         'gender': 'male',
#         'status': 'active'
#     }, {
#         'id': 3040,
#         'name': 'Chitraksh Pandey',
#         'email': 'pandey_chitraksh@quigley.org',
#         'gender': 'male',
#         'status': 'inactive'
#     }, {
#         'id': 3039,
#         'name': 'Deepali Nair',
#         'email': 'nair_deepali@dubuque.net',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 3038,
#         'name': 'Vasudev Joshi',
#         'email': 'vasudev_joshi@emard.info',
#         'gender': 'male',
#         'status': 'inactive'
#     }, {
#         'id': 3037,
#         'name': 'Purushottam Asan',
#         'email': 'purushottam_asan@kris.net',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 3036,
#         'name': 'The Hon. Chinmayanand Johar',
#         'email': 'the_johar_hon_chinmayanand@smitham.io',
#         'gender': 'female',
#         'status': 'active'
#     }, {
#         'id': 3035,
#         'name': 'Aarya Ganaka',
#         'email': 'aarya_ganaka@adams.net',
#         'gender': 'female',
#         'status': 'active'
#     }]
# }