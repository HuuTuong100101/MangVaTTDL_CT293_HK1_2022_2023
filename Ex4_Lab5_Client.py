# Nguyễn Hữu Tường - B1910480

import socket
import threading

host = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

req = input("Nhập GET<Khoảng trắng>Tên file : Để in ra nội dung file\n\
Nhập DELETE<Khoảng trắng>Tên file : Để xóa file\n\
Nhập LIST<Khoảng trắng>Tên thư mục : Để in ra các file trong thư mục\n\
Nhập tại đây: ")

# Kết nối với cổng 8000
def connectServer8000():
    s.connect((host,8000))
    s.send(req.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print(data)

# Kết nối với cổng 8001
def connectServer8001():
    s1.connect((host,8001))
    data1 = s1.recv(1024).decode('utf-8')
    print(data1)

s8000 = threading.Thread(target=connectServer8000)
s8001 = threading.Thread(target=connectServer8001)

s8000.start()
s8001.start()