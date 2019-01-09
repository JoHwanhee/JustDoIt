from bottle import run, route, static_file
from api.todos import todoApi
from api.static import staticApi
from api.root import rootApi

class RestServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.running = False

    def run(self):
        if not self.running:
            rootApi.merge(todoApi)
            rootApi.merge(staticApi)
            run(rootApi, host=self.host, port=self.port)
            self.running = True

    # todo : i don't know how to stop the server
    def stop(self):
        if self.running:
            self.running = False

