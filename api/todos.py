from bottle import Bottle, response
from api import restUtils
from data.TodoManager import TodoManager
import json

todoApi = Bottle()
_json_data = TodoManager().json


@todoApi.get("/todos")
def listing_handler():
    jsonString = json.loads(_json_data)

    restUtils.set_header_json(response)
    restUtils.set_access_control(response)

    return jsonString


@todoApi.post("/todos")
def create_todo():
    pass


@todoApi.put("/todos/<memoNumber>")
def update_todo(number):
    pass


@todoApi.delete("/todos/<memoNumber>")
def delete_todo(number):
    pass

