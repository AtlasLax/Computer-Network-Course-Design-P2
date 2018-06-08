#!/usr/bin/python
# -*- coding:utf-8 -*-


def addr_recv(server):
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
    server.close()


# Message receive
def msg_recv(server):

    # Receive the 2nd send:client's IP address
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))

    # Receive the 3rd send:client's message
    msg = server.recv(1024)
    print("  Message:%s" % msg.decode('utf-8'))

    # Closing this connection
    server.close()


#File receive
def file_recv(server):

    # Receive the 2nd send:client's IP address
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))

    # Receive the 3rd send:file receive path and name
    file_name = server.recv(1024).decode("utf-8")
    print("Start receiving to", file_name)

    # Start to write (write binary)
    file=open(file_name,'wb')

    # Receive all buffer sended by client
    while True:
        data=server.recv(1024)

        # If buffer is empty
        if not data:
            break
        file.write(data)

    # File writing complete
    # Closing this connection
    file.close()
    print("receiving %s successful" % file_name)



