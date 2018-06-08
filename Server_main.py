#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import Server_tools
import threading


server_ip1 = "192.168.3.135"
server_port1 = 8001
server_port2 = 10000
server_port3 = 9000


server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((server_ip1,server_port3))
server.listen(5)
print("your ip",server_ip1)


while True:

    """
    conn, addr1 = message.accept()
    target, addr2 = file.accept()
    Server_tools.addr_recv(message)
    Server_tools.msg_recv(msg, message)
    dispose = threading.Thread(target=Server_tools.recv_file, args=(target,))
    dispose.start()
    """

    target, addr3 = server.accept()

    flag = target.recv(1024)

    print(flag.decode("utf-8"))
    if flag.decode("utf-8") == "file":
        dispose = threading.Thread(target=Server_tools.file_recv, args=(target,))
        dispose.start()

    elif flag.decode("utf-8") == "msg":
        dispose = threading.Thread(target = Server_tools.msg_recv, args=(target,))
        dispose.start()

server.close()