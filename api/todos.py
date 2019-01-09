from bottle import Bottle, response
from api import utils
import json

todoApi = Bottle()

_file_directory = 'F:\\JustDoIt\\data\\todos.json'
_json_data = open(_file_directory, encoding='UTF8').read()


@todoApi.get("/todos")
def listing_handler():
    jsonString = json.loads(_json_data)

    response.set_header("Content-Type", "application/json; charset=utf-8")
    response.set_header("Cache-Control", "no-cache")

    utils.set_access_control(response)

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

