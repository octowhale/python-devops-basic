#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@python_version: python3.6
@file: socket_client.py
@time: 2017/8/11 11:43
"""

import os
import sys
import socket


def client(host='localhost',port=30086):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        msg = bytes(input(">>: "), encoding='utf8')
        s.sendall(msg)
        data = s.recv(1024)
        print('Received ', repr(data))


if __name__ == '__main__':
    client()
