# -*- coding: utf-8 -*-
__author__ = 'sencer'


import websocket
import thread
import time
import sys


def on_message(ws, message):
    print message


def on_error(ws, error):
    print error


def on_close(ws):
    print "### closed ###"


def on_open(ws, count):
    def run(*args):
        while True:
            # send the message, then wait
            # so thread doesnt exit and socket
            # isnt closed
            ws.send("Hello, this is Nr: {}".format(count))

        time.sleep(5)
        ws.close()
        print("Thread terminating...")
        sys.exit()

    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    host = "ws://localhost:8888/ws"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

