# Nguyễn Hữu Tường - B1910480

import socket

URL = "www.cit.ctu.edu.vn"
socket_create = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_create.connect((URL,80))
msg = "GET / HTTP/1.0\r\n\r\n".encode()
socket_create.send(msg)
HTML = socket_create.recv(10000)
print(HTML.decode())
socket_create.close()