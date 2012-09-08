import socket

from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.python_fixes import makefile
import uwsgi


class WSGIMiddlewareHandler(WebSocketHandler):
    def __init__(self, environ, start_response, application):
        self.environ = environ
        self.socket = socket.fromfd(uwsgi.connection_fd(), socket.AF_INET, socket.SOCK_STREAM)
        self.rfile = makefile(self.socket)
        self.application = application
        self.start_response = start_response
        self.request_version = environ['SERVER_PROTOCOL']

    def log_request(self):
        pass


def ws_middleware(wrapped_app):
    def application(environ, start_response):
        handler = WSGIMiddlewareHandler(environ, start_response, wrapped_app)
        upgrade = environ.get('HTTP_UPGRADE', '').lower()
        if upgrade == 'websocket':
            connection = environ.get('HTTP_CONNECTION', '').lower()
            if 'upgrade' in connection:
                return handler._handle_websocket()
        return wrapped_app(environ, start_response)
    return application
