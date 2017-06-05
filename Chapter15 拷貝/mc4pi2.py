# L-40 MCS 260 Wed 20 Apr 2016 : mc4pi2.py

"""
Implements server for Monte Carlo method for pi,
with two clients.  Server dispatches the seeds
and collects results.
"""
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = ''   # blank so any address can be used
NUMBER = 11267  # number for the port
BUFFER = 80     # size of the buffer

SERVER_ADDRESS = (HOSTNAME, NUMBER)
SERVER = Socket(AF_INET, SOCK_STREAM)
SERVER.bind(SERVER_ADDRESS)
SERVER.listen(2)

print('server waits for connections...')

FIRST, FIRST_ADDRESS = SERVER.accept()
SECOND, SECOND_ADDRESS = SERVER.accept()

FIRST.send('1'.encode())
SECOND.send('2'.encode())

print('server waits for results...')

PART1 = FIRST.recv(BUFFER).decode()
PART2 = SECOND.recv(BUFFER).decode()

RESULT = 2*(float(PART1)+float(PART2))
print('approximation for pi =', RESULT)

SERVER.close()
