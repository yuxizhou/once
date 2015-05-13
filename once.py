__author__ = 'yu'

from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler


class OnceWebSocket(WebSocketHandler):
    def on_message(self, message):
        pass

    def on_close(self):
        pass


class Application(Application):
    def __init__(self):
        handlers = [
            (r"/ws", OnceWebSocket)
        ]

        settings = dict(
            debug=False
        )

        Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    http_server = HTTPServer(Application())
    http_server.listen(8888)

    IOLoop.instance().start()