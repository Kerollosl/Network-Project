import socket

# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 7777))

fileName, addr = server.recvfrom(1024)
print(fileName.decode('utf-8'))
fileSize = server.recvfrom(1024)[0].decode('utf-8')
print(fileSize)

# Open a file to write the received data
file = open(fileName, "wb")
total_data = 0

while total_data < int(fileSize):
    # Receive data from the client
    data, addr = server.recvfrom(1024)
    if not data:
        break

    # Write the received data to the file
    file.write(data)
    total_data += len(data)

    # Send an acknowledgment back to the client
    server.sendto(b"ACK", addr)

file.close()
print(f"File received from {addr}")
