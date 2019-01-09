from webServer.RestServer import RestServer

# todo : load data from .ini file
if __name__ == "__main__":
    server = RestServer('127.0.0.1', 8000)
    server.run()
