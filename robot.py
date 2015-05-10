# -*- coding: utf-8 -*-
import time

__author__ = 'Sencer HAMARAT'


import websocket
import thread


def onmessage(ws, message):
    print message


def onerror(ws, error):
    print error


def onclose(ws):
    print "Bağlantı kapatıldı."


def onopen(ws, count):
    def run(*args):
        ws.send("Berhaba ben {}. istemci".format(count))
    thread.start_new_thread(run, ())
    time.sleep(1)

if __name__ == "__main__":
    i = 0
    while i < 10000:
        i += 1
        websocket.enableTrace(False)
        host = "ws://localhost:9090/ws"
        ws = websocket.WebSocketApp(host,
                                    on_message=onmessage,
                                    on_error=onerror,
                                    on_close=onclose)
        ws.on_open = onopen
        ws.run_forever()
