import socket

Host = socket.gethostname() #localhost
Port = 8888
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((Host,Port))
server_socket.listen(5)
print("Server is listening ...")

connect, address = server_socket.accept()
print("Connected with", address)

data_Client = connect.recv(10000).decode()

def numbers_to_strings(argument):
    switcher = {
        "0": "khong",
        "1": "mot",
        "2": "hai",
        "3": "ba",
        "4": "bon",
        "5": "nam",
        "6": "sau",
        "7": "bay",
        "8": "tam",
        "9": "chin",
    }
    return switcher.get(argument, "Khong phai so nguyen")

result = numbers_to_strings(data_Client)
connect.send(result.encode())

connect.close()