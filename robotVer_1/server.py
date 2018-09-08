#coding=utf-8
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import socket
import time

host = '127.0.0.1'
port = 8088
BUFFSIZE = 1024
Addr = (host, port)

ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_sock.bind(Addr)
ser_sock.listen(5)

while True:
    print("waiting for connint ....")
    cli_sock, addr = ser_sock.accept()
    while True:
        data = cli_sock.recv(BUFFSIZE).decode()
        if not data:
            break
        cli_sock.send("你好，我是服务器".encode())
    cli_sock.close()
ser_sock.close()
