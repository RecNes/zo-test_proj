#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import argparse
from robot import RobotLoader


__author__ = 'Sencer HAMARAT'


def set_up_logging(args):
    log_format = '%(created)f | %(message)s'
    logging.basicConfig(format=log_format)
    logger = logging.getLogger("loader")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(args.output_file, mode='w')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('  %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def setup_cmd_parser():
    p = argparse.ArgumentParser(description='Robot loader.')
    p.add_argument('-i', '--ip', action='store', default='localhost', help='Server IP address.')
    p.add_argument('-p', '--port', action='store', type=int, default=9090, help='Server Port.')
    p.add_argument('-c', '--clients', action='store', type=int, default=10000, help='Number of clients.')
    p.add_argument('-n', '--connect_rate', action='store', type=float, default=10,
                   help='Connect rate (connections/sec).')
    p.add_argument('-s', '--send_rate', action='store', type=float, default=10, help='Send rate (messages/sec).')
    p.add_argument('-o', '--output_file', action='store', default='loader.log', help='Name of log file.')
    return p

if __name__ == "__main__":
    PARSER = setup_cmd_parser()
    ARGS = PARSER.parse_args()
    log = set_up_logging(ARGS)
    log.info("START_LOADING - PID:%d" % (os.getpid(),))

    log.info("LOADING_PARAMS - IP:%s - PORT:%s - CLIENTS:%s - SEND_RATE:%s" %
             (ARGS.ip, ARGS.port, ARGS.clients, ARGS.send_rate))

    cs = RobotLoader(ARGS.ip, ARGS.port, num_clients=ARGS.clients,
                     connect_rate=ARGS.connect_rate, send_rate=ARGS.send_rate)
    cs.instantiate_clients()
    cs.start_all_clients()
    cs.connect_all_clients()
    cs.start_sending()
    raw_input("Press ENTER to finish...")
    cs.finish_clients()