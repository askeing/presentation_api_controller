#!/usr/bin/env python

# Client for testing

import sys
import socket


print('\rEnter host: '),
host = sys.stdin.readline()

print('\rEnter port: '),
port = int(sys.stdin.readline())

# create client, connect to controller
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print('\rConnected.\n')

# client receive data
client_received = client.recv(1024)
print('Recv: {}'.format(client_received))

# client send message to controller
msg = 'Hi! This is client. How are you?'
client.sendall(msg)
print('Send: {}'.format(msg))

# client receive data
client_received = client.recv(1024)
print('Recv: {}'.format(client_received))

# close
client.close()
