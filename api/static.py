from bottle import Bottle, static_file

staticApi = Bottle()


@staticApi.route('/static/<path:path>')
def add_static_service(path):
    return static_file(path, root='./static/')

