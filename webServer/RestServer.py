from bottle import run
from api import todos


class RestServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.running = False

    def run(self):
        if not self.running:
            run(todos.todoApi, host=self.host, port=self.port)
            self.running = True

    # todo : i don't know how to stop the server
    def stop(self):
        if self.running:
            self.running = False