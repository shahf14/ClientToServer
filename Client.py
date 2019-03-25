# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:21:01 2019

@author: shahf
"""
import socket
import random
import logging

logging.basicConfig(filename = 'Client_Record.log',level=logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')
msg = str(random.randint(1,100))
logging.info("Message created successfully")
with socket.socket(socket.SOCK_DGRAM) as s:
    logging.info("Message created successfully")
    s.connect(('127.0.0.1', 65432))
    s.sendall(msg.encode('utf-8'))
    logging.info("Message Coded and sent")

    data = s.recv(1024)

print('Received', repr(data))