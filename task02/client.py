import socket
import threading
import sys

SERVER_IP = sys.argv[1]
PORT = int(sys.argv[2])
ROLE = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

client.send(ROLE.encode())


def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()

            if msg:
                print(f"\nReceived: {msg}")

        except:
            break


if ROLE == "SUBSCRIBER":
    threading.Thread(
        target=receive_messages,
        daemon=True
    ).start()


while True:

    msg = input()

    if msg.lower() == "terminate":
        client.close()
        break

    if ROLE == "PUBLISHER":
        client.send(msg.encode())