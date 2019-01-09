_allow_origin = "*"
_allow_methods = "PUT, GET, POST, DELETE, OPTIONS"
_allow_headers = "Authorization, Origin, Accept, Content-Type, X-Requested-With"


def set_access_control(response):
    response.set_header("Access-Control-Allow-Origin", _allow_origin)
    response.set_header("Access-Control-Allow-Methods", _allow_methods)
    response.set_header("Access-Control-Allow-Headers", _allow_headers)