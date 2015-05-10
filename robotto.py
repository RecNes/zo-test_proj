# -*- coding: utf-8 -*-
import time

__author__ = 'Sencer HAMARAT'


import websocket
import thread


def onmessage(ws, message):
    """
    Sunucudan gelen mesajları konsola basar
    :param ws:
    :param message:
    :return:
    """
    print message


def onerror(ws, error):
    """
    Socket bağlantısı hatasında konsola bilgi basar
    :param ws:
    :param error:
    :return:
    """
    print error


def onclose(ws):
    """
    Socket bağlantısı kesildiğinde konsola bilgi basar
    :param ws:
    :return:
    """
    print "Bağlantı kapatıldı."


def onopen(ws, count):
    """
    Yeni bir thread oluşturup socket bağlantısı açar ve sunucuya mesaj gönderir
    :param ws:
    :param count:
    :return:
    """
    def run(*args):
        ws.send("Berhaba ben {}. istemci".format(count))
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(False)
    host = "ws://localhost:9090/ws"
    ws = websocket.WebSocketApp(host,
                                on_message=onmessage,
                                on_error=onerror,
                                on_close=onclose)
    ws.on_open = onopen
    ws.run_forever()
