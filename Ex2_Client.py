import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8888
socket_client.connect((host,port))

data_send = input("Nhập vào 1 số từ 0 - 9: ")

socket_client.send(data_send.encode())

data_recv = socket_client.recv(10000).decode()

print(data_recv)
socket_client.close()
