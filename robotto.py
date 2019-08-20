# -*- coding: utf-8 -*-
import time

__author__ = 'Sencer HAMARAT'


import websocket
from threading import Thread
import sys


def onmessage(ws, message):
    """
    Print server messages to console
    :param ws:
    :param message:
    :return:
    """
    print(message)


def onerror(ws, error):
    """
    Print information on socket connection error
    :param ws:
    :param error:
    :return:
    """
    print(error)


def onclose(ws):
    """
    Print information on socket connection closed
    :param ws:
    :return:
    """
    print("Connection Closed.")


def onopen(ws, count):
    """
    Create new socket connetion thread and send message to server
    :param ws:
    :param count:
    :return:
    """
    def run(*args):
        ws.send("Hello, this is {}. client".format(count))
    Thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(False)
    args = sys.argv
    if len(args) > 1:
        address = args[1]
    else:
        address = "localhost"
        print("< localhost > is the default address.")
        print("To set address manually run as < python robotto.py 192.168.1.x >.")
        print("To display current address run < python show_ip.py >.")

    host = "ws://{}:9090/ws".format(address)
    ws = websocket.WebSocketApp(host,
                                on_message=onmessage,
                                on_error=onerror,
                                on_close=onclose)
    ws.on_open = onopen
    ws.run_forever()
