import json


class JsonUtils:
    @classmethod
    def is_json(cls, json_string):
        try:
            json_object = json.loads(json_string)
        except ValueError as e:
            return False
        return True