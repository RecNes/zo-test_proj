#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

__author__ = 'Remind Bird'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
print s.getsockname()[0]
