from bottle import Bottle, response
from api import restUtils
from data.TotoManager import TodoManager
import json

todoApi = Bottle()
_json_data = TodoManager().json


@todoApi.get("/todos")
def listing_handler():
    jsonString = json.loads(_json_data)

    restUtils.set_header_json(response)
    restUtils.set_access_control(response)

    return jsonString


@todoApi.post("/todos/categories")
def create_category():
    pass


@todoApi.post("/todos/<categoryNumber>/memos/<memoNumber>")
def create_memo():
    pass


@todoApi.put("/todos/<categoryNumber>")
def update_category(number):
    pass


@todoApi.put("/todos/<categoryNumber>/memos/<memoNumber>")
def update_memo(memoNumber):
    pass


@todoApi.delete("/todos/<categoryNumber>")
def delete_category(number):
    pass


@todoApi.delete("/todos/<categoryNumber>/memos/<memoNumber>")
def delete_memo(memoNumber):
    pass

