#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import time


server_ip1 = "192.168.3.135"
client_ip1 = "192.168.3.135"
server_port1 = 8001
server_port2 = 10000
server_port3 = 9000


def addr_send():
    add = client_ip1
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip1, server_port3))
    client.send(add.encode("utf-8"))
    # Send msg transmission flag
    client.send(client_ip1.encode("utf-8"))
    # print('Address: ', add)
    client.close()


def msg_send():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip1, server_port3))

    # Send msg transmission flag -- 1st send
    client.send("msg".encode("utf-8"))
    time.sleep(1)

    # Send IP -- 2nd send
    client.send(client_ip1.encode("utf-8"))
    time.sleep(1)

    print('_' * 50)
    print("_" * 19 + "Message Send" + "_" * 19)
    print("Input:")

    msg = input()
    # Send message -- 3rd send
    client.send(msg.encode("utf-8"))
    time.sleep(1)
    # print('Message: ', msg)
    print(" " * 22 + "Sended")
    print("")
    client.close()
    if msg == "DCDC":
        return 1


def file_send():
    host = server_ip1

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, server_port3))

    # Send file transmission flag -- 1st send
    client.send("file".encode("utf-8"))
    time.sleep(1)

    # Send IP -- 2nd send
    client.send(client_ip1.encode("utf-8"))
    time.sleep(1)

    print('_' * 50)
    print("_" * 20 + "File Send" + "_" * 21)
    file = input("Input path of the file:")
    path = input("Input target location(inlude file's name) of the file:")

    # Send path & name -- 3rd send
    client.send(path.encode("utf-8"))
    time.sleep(1)

    file = open(file, "rb")

    # Send file through buffer
    while True:
        file_buffer = file.read(1024)
        if not file_buffer:
            break
        client.send(file_buffer)

    client.close()
    print("\nSuccessful")



