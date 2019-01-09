from bottle import Bottle, static_file

rootApi = Bottle()


@rootApi.route('/')
def root():
    return static_file('index.html', root='./')

