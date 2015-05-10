# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

__author__ = 'Sencer HAMARAT'


class MainHandler(tornado.web.RequestHandler):
    """
    İstek yapıldığında index.html'i istemciye gönderir.
    """
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())


class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()  # Clientların açtığı ger bir bağlantının listesini tutacak liste.

    def check_origin(self, origin):
        """
        Cross site kontrolünü devre dışı bırakır. Ön tanımlı olarak güvenlik sebebiyle kontrol vardır.
        Script'in her şekilde çalışması için bu kısmı atlattım.
        :param origin:
        :return:
        """
        return True

    def open(self):
        """
        Her istemci isteğine bir bağlantı açar ve bağlantının kabul edildiğine dair istemciye mesaj gönderir
        Ve tüm clientları yeni istemcinin numarası iel birlikte sunucuya dahil olduğundan haberdar eder.
        :return:
        """
        
        self.connections.add(self)
        self.write_message("Sunucu: Bağlantı kuruldu.")
        for con in self.connections:
            con.write_message('{}. istemci bağlandı'.format(str(len(self.connections))))
        print 'Yeni bağlantı kuruldu...'

    def on_message(self, message):
        """
        Herhangi bir istemciden gelen mesajları tüm diğer istemcilere gönderir.
        :param message:
        :return:
        """
        msj = u' '.join((message,)).encode('utf-8').strip()
        for con in self.connections:
            con.write_message('Websitesndeki kullanıcı diyor ki: {}'.format(msj))

    def on_close(self):
        """
        Sunucu çıktılarında bağlantının kapatıldığını gösterir.
        :return:
        """
        print 'connection closed...'


# Tornado sunucusunun URL yapılandırması:
application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./"}),  # static dosya sağlayıcı.
])

if __name__ == "__main__":
    application.listen(9090)  # Tornado sunucusunu uygulama olarak 9090 portunu dinlemek üzere çalıştırır
    tornado.ioloop.IOLoop.instance().start()  # Sunucunun devamlı olarka çalışmasını sağlar