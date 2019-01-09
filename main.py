from webServer.RestServer import RestServer

if __name__ == "__main__":
    server = RestServer('127.0.0.1', 8000)
    server.run_server()
