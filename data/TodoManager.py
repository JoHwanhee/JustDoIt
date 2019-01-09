import json
_file_directory = 'F:\\JustDoIt\\data\\todos.json'


class TodoManager:
    def __init__(self):
        json_data = open(_file_directory, encoding='UTF8').read()
        self.json_data = json.loads(json_data)

    def get_todo(self):
        return json.dumps(self.json_data)

    def add_todo(self, memo):
        todo = {
            "memo": memo,
            "done": False
        }

        self.json_data['todos'].append(todo)

    def remove_todo(self, memoNumber):
        del self.json_data['todos'][int(memoNumber)]

    def update_todo(self, memoNumber):
        pass