import threading
import socket
import time

host = '127.0.0.1'
port = 8000

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketUDP.bind((host,port))
conn, addr = socketUDP.recvfrom(1024)
socketUDP.sendto('Server: Hello Client!'.encode(), addr)
print(conn.decode())

def sendmsg():
    while True:
        msg = input()
        socketUDP.sendto(("Server: " + msg + ' ' + "( " +time.ctime(time.time()) + ")").encode(), addr)

def receivemsg():
    while True:
        data, addr = socketUDP.recvfrom(1024)
        msg = data.decode()
        print(msg)

t1 = threading.Thread(target=receivemsg)
t2 = threading.Thread(target=sendmsg)
t1.start()
t2.start()