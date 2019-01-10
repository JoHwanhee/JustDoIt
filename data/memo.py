import json
from ..utils.jsonUtils import JsonUtils


class Memo:
    def __init__(self):
        self.memo = ""
        self.id = ""
        self.done = False

    def to_json(self):
        json_object = {
           "memo": self.memo,
            "id": self.id,
            "done": self.done
        }

        return json_object

    @classmethod
    def create_from(cls, json_string):
        if JsonUtils.is_json(json_string):
            json_object = json.loads(json_string)
            memo = Memo()
            memo.done = json_object["done"]
            memo.memo = json_object["memo"]
            memo.id = json_object["id"]
            return memo
        else:
            print('cannot parse to json')
            return None
