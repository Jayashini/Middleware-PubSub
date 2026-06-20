import socket
import threading
import sys
import time

BROKERS = [
    ("127.0.0.1", 5000),
    ("127.0.0.1", 5001),
    ("127.0.0.1", 5002)
]

ROLE = sys.argv[1].upper()
TOPIC = sys.argv[2].upper()

client = None
connected_broker = None


def connect_to_broker():

    global client
    global connected_broker

    while True:

        for host, port in BROKERS:

            try:

                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                sock.connect((host, port))

                sock.send(
                    f"{ROLE}|{TOPIC}".encode()
                )

                client = sock
                connected_broker = port

                print(f"\nConnected to Broker {port}")

                return

            except:
                continue

        print("No brokers available. Retrying in 3 seconds...")
        time.sleep(3)


def receive_messages():

    global client

    while True:

        try:

            msg = client.recv(1024).decode()

            if not msg:
                raise Exception()

            print(f"\n{msg}")

        except:

            print(
                f"\nBroker {connected_broker} unavailable."
            )

            connect_to_broker()


connect_to_broker()

if ROLE == "SUBSCRIBER":

    threading.Thread(
        target=receive_messages,
        daemon=True
    ).start()


while True:

    try:

        message = input("Enter message: ")

        if message.lower() == "terminate":
            client.close()
            break

        if ROLE == "PUBLISHER":
            client.send(message.encode())

    except:

        print(
            f"\nBroker {connected_broker} unavailable."
        )

        connect_to_broker()