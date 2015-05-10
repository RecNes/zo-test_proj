# -*- coding: utf-8 -*-
import time

__author__ = 'Sencer HAMARAT'


import websocket
import thread
import sys


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
    args = sys.argv
    if len(args) > 1:
        address = args[1]
    else:
        address = "localhost"
        print "Ön tanımlı adres < localhost > olarak kullanılır."
        print "Adres belirtmek için < python robotto.py 192.168.1.x > şeklinde yazınız."
        print "Sunucunun IP adresini görmek için < python show_ip.py > kullanabilirsiniz."

    host = "ws://{}:9090/ws".format(address)
    ws = websocket.WebSocketApp(host,
                                on_message=onmessage,
                                on_error=onerror,
                                on_close=onclose)
    ws.on_open = onopen
    ws.run_forever()
