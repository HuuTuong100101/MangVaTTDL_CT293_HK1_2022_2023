import threading
import socket
import time

host = '127.0.0.1'
port = 8000

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketUDP.sendto('Client: Hello Server!'.encode(), (host,port))
conn, addr = socketUDP.recvfrom(1024)
print(conn.decode())

def sendmsg():
    while True:
        msg = input()
        socketUDP.sendto(("Client: " + msg + ' ' + "( " +time.ctime(time.time()) + ")").encode(), (host,port))

def receivemsg():
    while True:
        data, addr = socketUDP.recvfrom(1024)
        msg = data.decode()
        print(msg)

t1 = threading.Thread(target=receivemsg)
t2 = threading.Thread(target=sendmsg)
t1.start()
t2.start()