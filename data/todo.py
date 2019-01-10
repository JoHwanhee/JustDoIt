import json
from .memo import Memo
from utils.jsonUtils import JsonUtils


class Todo:
    def __init__(self):
        self.categories = []
        self.updated = ''

    def to_json(self):
        json_object = {
            "categories": self.categories,
            "updated": self.updated
        }

        return json_object

    def add(self, input_category, input_memo):
        found = False
        for value in self.categories:
            if value.category == input_category.category:
                value.add(input_memo)
                found = True

        if not found:
            input_category.add(input_memo)
            self.categories.append(input_category)

    @classmethod
    def create_from(cls, json_string):
        if JsonUtils.is_json(json_string):
            json_object = json.loads(json_string)

            todo = Todo()
            todo.categories = json_object["categories"]
            todo.updated = json_object["updated"]

            return todo
        else:
            print('cannot parse to json')
            return None
