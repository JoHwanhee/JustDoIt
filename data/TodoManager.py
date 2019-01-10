from .todo import Todo

import json
_file_directory = 'F:\\JustDoIt\\data\\todos.json'


class TodoManager:
    def __init__(self):
        json_data = open(_file_directory, encoding='UTF8').read()
        self.todo = Todo.create_from(json_data)
        print(self.todo)

    def get_todo(self):
        return self.todo.to_json()

    def add_todo(self, category, memo):
        self.todo.add(category, memo)

    def remove_todo(self, memoNumber):
        del self.json_data['todos'][int(memoNumber)]

    def update_todo(self, memoNumber):
        pass

