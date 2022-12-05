# Nguyễn Hữu Tường - B1910480
import socket
import threading
import os
host = '127.0.0.1'
port1 = 8000
port2 = 8001
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# chạy server ở cổng 8001
def server8001():
    s2.bind((host,8001))
    s2.listen(5)
    print("Server 8001 is listening")

# chạy server ở cổng 8000
def server8000():
    s1.bind((host,8000))
    s1.listen(5)
    print("Server 8000 is listening")
    
def handleClient():
    # Khởi chạy server ở cổng 8000
    server8000()
    connect1,addr1 = s1.accept()
    print("Connected with ", addr1)
    data = connect1.recv(1024).decode('utf-8')

    # Khởi chạy server ở công 8001
    newSocket = threading.Thread(target=server8001)
    newSocket.start()
    newSocket.join()
    connect2,addr2 = s2.accept()
    print("Connected with ", addr2)

    check = os.path.exists(data.split()[1])
    if(check == True):
        # Dữ liệu sau khi xử lý yêu cầu của client
        dataReplyClient = handleRequest(data.split()[0], data.split()[1])
        # Gửi msg về client qua cổng 8000
        msg = threading.Thread(target=send, args=("OK\n".encode(), connect1))
        msg.start()
        msg.join()
        # Gửi data về client qua cổng 8001
        dataClient = threading.Thread(target=send, args=(dataReplyClient,connect2))
        dataClient.start()
        dataClient.join()
    else:
        # Không tìm thấy file/folder
        send("ERROR\n".encode('utf-8'),connect1)

# xứ lý yêu cầu của client
def handleRequest(req, fileName):
    if req == "GET":
        result = open(fileName,'rb').read(1024)
    elif req == "DELETE":
        os.remove(fileName)
        result = "Xóa thành công".encode('utf-8')
    else:
        listdir = os.listdir(fileName)
        result = ("\n".join(listdir)).encode('utf-8')
    return result
# Gởi dữ liệu về client
def send(data,conn):
    conn.send(data)

def main():
    handleClient()
    s1.close()
    s2.close()

main()