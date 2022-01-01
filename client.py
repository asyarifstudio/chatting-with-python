import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1" #localhost, artinya program server kita jalan di PC yang sama
serverPort = 2222 #port yang sama dengan server

handlerSocket.connect((serverIP,serverPort))
print 'terkoneksi ke server'

while True:
    message = handlerSocket.recv(1024) #terima 1024 karakter dari server
    print 'pesan dari server :',message
    message = raw_input('masukkan pesan anda : ')
    handlerSocket.send(message)
    pass