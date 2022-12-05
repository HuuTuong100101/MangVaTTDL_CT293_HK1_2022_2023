import socket
import threading

Host = socket.gethostname() #localhost
Port = 8888

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

def handle_client(connect, address):
    data_Client = connect.recv(10000).decode()
    result = numbers_to_strings(data_Client)
    connect.send(result.encode())
    connect.close()

def main():
    print("Server is listening ...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((Host,Port))
    server_socket.listen(5)

    while True:
        connect, address = server_socket.accept()
        print("Connected with", address)
        thread = threading.Thread(target=handle_client, args=(connect, address))
        thread.start()

if __name__ == "__main__":
    main()