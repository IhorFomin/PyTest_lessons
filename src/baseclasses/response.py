# from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                # validate(item, schema)
                schema.parse_obj(item)
        else:
            # validate(self.response_json, schema)
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return \
            f"\nStatyus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"
