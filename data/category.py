import json
from .memo import Memo
from ..utils.jsonUtils import JsonUtils


class Category:
    def __init__(self):
        self.memoList = []
        self.category = ''

    def to_json(self):
        json_object = {
            "memoList": [],
            "category": self.category
        }

        memoList = []
        for memo in self.memoList:
            memoList.append(memo.to_json())

        json_object["memoList"] = memoList

        return json_object

    def add(self, memo):
        self.memoList.append(memo)

    @classmethod
    def create_from(cls, json_string):
        if JsonUtils.is_json(json_string):
            json_object = json.loads(json_string)
            category = Category()
            category.memoList = json_object["memoList"]
            category.category = json_object["category"]
            return category
        else:
            print('cannot parse to json')
            return None
