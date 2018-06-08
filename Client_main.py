#!/usr/bin/python
# -*- coding:utf-8 -*-

import Client_tools


flag = 0
print("Input 'DCDC' to exit")
while True:
    choice = 0
    print("1.Messeage send")
    print("2.File send")
    choice = input("Input your choice:")
    if choice in['0', '1', '2']:
        if choice == '1':
            flag = 0
            flag = Client_tools.msg_send()

        if choice == '2':
            Client_tools.file_send()

    if flag == 1:
        break




