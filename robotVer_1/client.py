#coding=utf-8

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import socket
from client1 import *


class Client(Ui_Form, QWidget):
    def __init__(self):
        super(Client, self).__init__()
        self.setupUi(self)
        self.port = 8088
        self.host = '127.0.0.1'
        self.Buffsize = 1024
        self.type = 0 # 0 是断开连接， 1是建立了连接
        self.addr = (self.host, self.port)
    def connect_server(self):
        if self.type == 0:
            self.cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.cli_sock.connect(self.addr)
            self.type = 1
            self.textBrowser.append("连接服务器成功")
        else:
            QMessageBox.about(self, "警告", "连接已经建立，不能重复建立")
    def chat_with_server(self):
        if self.type == 1:
            data = self.lineEdit.text()
            print(data)
            if data:
                self.cli_sock.send(data.encode())
                self.textBrowser.append("我说："+data)
                self.lineEdit.clear()
                self.lineEdit.setFocus()
                answer = self.cli_sock.recv(self.Buffsize).decode()
                if answer:
                    self.textBrowser.append("服务器回复："+ answer)
            else:
                QMessageBox.about(self, "警告", "输入内容为空")
        elif self.type == 0:
            QMessageBox.about(self, "警告", "你已关闭连接，需重新建立")
    def close_server(self):
        if self.type == 1:
            self.textBrowser.append("再见")
            self.cli_sock.close()
            self.type = 0
        else:
            QMessageBox.about(self, "警告", "连接已经关闭")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    one = Client()
    one.connect_pushButton.clicked.connect(one.connect_server)
    one.close_pushButton.clicked.connect(one.close_server)
    one.pushButton.clicked.connect(one.chat_with_server)
    one.show()
    sys.exit(app.exec_())

