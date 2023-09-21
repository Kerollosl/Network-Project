import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file = open("bmp.bmp", "rb")
fileSize = os.path.getsize("bmp.bmp")

client.sendto("received_IMG.bmp".encode('utf-8'), ("127.0.0.1",7777))
client.sendto(str(fileSize).encode('utf-8'), ("127.0.0.1",7777))

for i in range(0,30):
    data = file.read(1024)
    client.sendto(data, ("127.0.0.1",7777))

file.close()
client.close()