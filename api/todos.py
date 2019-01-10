from bottle import Bottle, response, request
from data.TodoManager import TodoManager
import json

todoApi = Bottle()
_manager = TodoManager()
_allow_origin = "*"
_allow_methods = "PUT, GET, POST, DELETE, OPTIONS"
_allow_headers = "Authorization, Origin, Accept, Content-Type, X-Requested-With"



def set_response():
    response.set_header("Content-Type", "application/json; charset=utf-8")
    response.set_header("Cache-Control", "no-cache")
    response.set_header("Access-Control-Allow-Origin", _allow_origin)
    response.set_header("Access-Control-Allow-Methods", _allow_methods)
    response.set_header("Access-Control-Allow-Headers", _allow_headers)


@todoApi.get("/todo")
def listing_handler():
    json_string = _manager.get_todo()

    set_response()

    return json_string


@todoApi.post("/todo/categories")
def create_todo():

    set_response()

    return "ok"


@todoApi.post("/todo/categories/<category>")
def create_todo(category):

    set_response()

    return "ok"


@todoApi.put("/todo/<memoNumber>")
def update_todo(number):
    pass


@todoApi.delete("/todo/<memoNumber>")
def delete_todo(memoNumber):
    _manager.remove_todo(memoNumber)
    set_response()

    return "ok"

