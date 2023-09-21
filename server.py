import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1",7777))

fileName,addr = server.recvfrom(1024)
print(fileName.decode('utf-8'))
fileSize = server.recvfrom(1024)[0].decode('utf-8')
print(fileSize)

file = open(fileName, "wb")
fileBytes = b""

for i in range(0,30):
    data = server.recv(1024)
    fileBytes += data

file.write(fileBytes)

server.close()