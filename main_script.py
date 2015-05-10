# -*- coding: utf-8 -*-
from tornado import websocket, httpserver, web, ioloop

__author__ = 'sencer'

external_storage = list()


class WSHandler(websocket.WebSocketHandler):
    clients = []

    def check_origin(self, origin):
        # Overriding request check from cross sites. By default it returns False beause of security reasons
        return True

    def open(self):
        self.clients.append(self)
        socket_count = str(len(self.clients))
        print 'Socket Count is {} now.'.format(socket_count)
        self.write_message("This is the {} conn".format(socket_count))

    def on_message(self, message):
        print 'Message {}'.format(message)

    def on_close(self):
        self.clients.remove(self)
        print 'Connection closed.'

application = web.Application([
        (r'/ws', WSHandler),
    ])


if __name__ == "__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()




