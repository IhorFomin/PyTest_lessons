import requests

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
