import socket
import threading
import json
import sys

topics = {}

def handle_client(client, role, topic):

    while True:
        try:

            msg = client.recv(1024).decode()

            if not msg:
                break

            print(f"[{topic}] {msg}")

            if role == "PUBLISHER":

                if topic in topics:

                    for sub in topics[topic]:

                        try:
                            sub.send(
                                f"[{topic}] {msg}".encode()
                            )

                        except:
                            pass

        except:
            break

    if role == "SUBSCRIBER":

        if topic in topics:

            if client in topics[topic]:
                topics[topic].remove(client)

    client.close()


PORT = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", PORT))
server.listen()

print(f"Server listening on {PORT}")

while True:

    client, addr = server.accept()

    info = client.recv(1024).decode()

    role, topic = info.split("|")

    print(f"{addr} -> {role} -> {topic}")

    if role == "SUBSCRIBER":

        if topic not in topics:
            topics[topic] = []

        topics[topic].append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, role, topic)
    )

    thread.start()