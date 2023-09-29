import os
import socket
import time

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(1.0)  # Set a timeout for receiving ACK/NACK

# Open the file to be sent
file = open("bmp.bmp", "rb")
fileSize = os.path.getsize("bmp.bmp")

client.sendto("received_IMG.bmp".encode('utf-8'), ("127.0.0.1", 7777))
client.sendto(str(fileSize).encode('utf-8'), ("127.0.0.1", 7777))

start_time = time.time()  # set a timer to measure the process time

total_data, i = 0, 0
while True:
    # Read a chunk of data from the file
    data = file.read(1024)
    if not data:
        break
    client.sendto(data, ("127.0.0.1", 7777))

    try:
    # Attempt to receive an ACK from the server with a timeout of 1 second
        ack, _ = client.recvfrom(1024)  # Receive acknowledgment

        # Check if the received acknowledgment is not "ACK"
        if ack != b"ACK":
            print("NACK received. Process did not complete")
            break
        total_data += len(data)
        i += 1
        print(f'PERCENT COMPLETION after {i} packets sent: {total_data / int(fileSize) * 100}%')
        if total_data / int(fileSize) * 100 == 100:
            print("Process Completed")

    # Handle a timeout situation where no ACK is received
    except socket.timeout:
        print("Timeout: No ACK received. Process did not complete")
        break

file.close()
client.close()

# Calculate and print the elapsed time for the data transfer
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
