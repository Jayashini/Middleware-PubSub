import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python client.py <SERVER_IP> <PORT>")
    sys.exit()

SERVER_IP = sys.argv[1]
PORT = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

while True:
    msg = input("Enter message: ")

    if msg.lower() == "terminate":
        client.close()
        print("Disconnected")
        break

    client.send(msg.encode())