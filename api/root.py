from bottle import Bottle, static_file

rootApi = Bottle()


@rootApi.route('/')
def root():
    return 'hello world!!!!!!!!'

