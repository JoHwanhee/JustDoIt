_file_directory = 'F:\\JustDoIt\\data\\todos.json'


class TodoManager:
    def __init__(self):
        self.json = open(_file_directory, encoding='UTF8').read()
