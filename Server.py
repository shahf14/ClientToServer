# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:12:33 2019

@author: shahf
"""


import socket
import logging

logging.basicConfig(filename = 'Server_Record.log',level=logging.INFO)
logger = logging.getLogger()

with socket.socket(socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 65432))
    s.listen()
    logger.info("The server successfully logged in and listened to clients ")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
 
            if not data:
                break
            conn.sendall(data)
logging.info("Connection has been closed ")