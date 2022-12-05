# Nguyễn Hữu Tường - B1910480

from asyncio.windows_events import NULL
import socket;
host = "127.0.0.1"
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
print("Waiting for client....")

def Calculation(OP, Operant1, Operant2):
    try:
        match OP:
            case "+":
                return int(Operant1) + int(Operant2)
            case "-":
                return int(Operant1) - int(Operant2)
            case "*":
                return int(Operant1) * int(Operant2)
            case "/":
                return int(Operant1) / int(Operant2)
    except:
        return "Phép toán không hợp lệ"
while True:
    try:
        dataClient, addressClient = s.recvfrom(1024)
        print("Connected with", addressClient)
        dataClientDecode = dataClient.decode('utf-8')
        if dataClientDecode == 'x':
            break
        result = str(Calculation(dataClientDecode.split()[0], dataClientDecode.split()[1], dataClientDecode.split()[2]))
        DataSendToClient = result.encode('utf-8')
        s.sendto(DataSendToClient,addressClient)
    except:
        continue
s.close()