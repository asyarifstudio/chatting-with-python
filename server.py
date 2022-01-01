import socket


listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

#bind IP dan port ke listener socket
listenerSocket.bind((serverIP,serverPort))
#listener socket mendengar semua data yang masuk ke IP dan Port yang sudah kita atur
listenerSocket.listen(0)
print 'server siap menerima client'
while True:
    #kode ini menunggu sampai ada client yg terhubung ke server kita
    handlerSocket, addr = listenerSocket.accept()
    print 'sebuah client baru terkoneksi dengan alamat : ', addr
    while True:
        messsage = raw_input("masukkan pesan anda : ") #bagian ini menerima input dari terminal
        handlerSocket.send(messsage) #mengirim pesan ke client
        messsage = handlerSocket.recv(1024) #terima 1024 karater dari client
        print 'pesan dari client : ',messsage
        pass
    pass

