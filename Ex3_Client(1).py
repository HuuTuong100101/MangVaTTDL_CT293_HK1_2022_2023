# Nguyễn Hữu Tường

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

check = ''
while check != 'x':
    check = False
    while check == False:
        cal = input("Nhập vào phép toán muốn thực hiện (ex: 100 + 200) :\n")
        Newcal = cal.split()
        if len(Newcal) == 3:
            check = True
            dataSendServer = Newcal[1] + ' ' + Newcal[0] + ' ' +  Newcal[2]
            break
        print("Phép toán không đúng định dạng vui lòng nhập lại\n")
    
    s.sendto(dataSendServer.encode('utf-8'), ("127.0.0.1",8888))
    dataReceiveServer,address = s.recvfrom(1024)

    print("Kết quả: ",dataReceiveServer.decode('utf-8'))
    print("-----------------------------------------------------")

    check = input("Nhập x để thoát chương trình hoặc bấm phím bất kỳ để tiếp tục: ")
    s.sendto(check.encode('utf-8'), ("127.0.0.1",8888))