# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

__author__ = 'Sencer HAMARAT'


class MainHandler(tornado.web.RequestHandler):
    """
    Sends index.html to client when requested.
    """
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())


class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()  # List of client connections.

    def check_origin(self, origin):
        """
        To make JavaScript would work cross site check disabled.
        :param origin:
        :return:
        """
        return True

    def open(self):
        """
        Open a connection ony each request and send response message to client. 
        Warns every client about new client with it's client number.
        :return:
        """
        
        self.connections.add(self)
        self.write_message("Server: Connection established.")
        for con in self.connections:
            con.write_message('{}. client connected'.format(str(len(self.connections))))
        print('New connection established...')

    def on_message(self, message):
        """
        Transmit messages to all clients received from any client. 
        :param message:
        :return:
        """
        msj = u' '.join((message,)).encode('utf-8').strip()
        for con in self.connections:
            con.write_message('User saying: {}'.format(msj))

    def on_close(self):
        """
        Displaying closed connections
        :return:
        """
        self.connections.remove(self)
        print('Connection closed...')


# Tornado server URL configuration:
application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./"}),  # static file supplier.
])

if __name__ == "__main__":
    application.listen(9090)  # Tornado server port setting.
    tornado.ioloop.IOLoop.instance().start()  # Keep server running.
