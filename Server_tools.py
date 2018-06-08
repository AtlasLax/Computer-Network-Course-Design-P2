#!/usr/bin/python
# -*- coding:utf-8 -*-


def addr_recv(server):
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
    server.close()


def msg_recv(server):
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
    msg = server.recv(1024)
    print("  Message:%s" % msg.decode('utf-8'))
    server.close()


def file_recv(server):
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))

    file_name = server.recv(1024).decode("utf-8")
    print("Start receiving to", file_name)

    file=open(file_name,'wb')

    while True:
        data=server.recv(1024)
        if not data:
            break
        file.write(data)
    file.close()
    print("receiving %s successful" % file_name)



