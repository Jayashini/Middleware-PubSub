import socket
import threading
import sys

subscribers = []

def handle_client(client, role):

    while True:
        try:
            msg = client.recv(1024).decode()

            if not msg:
                break

            print(msg)

            if role == "PUBLISHER":
                for sub in subscribers:
                    try:
                        sub.send(msg.encode())
                    except:
                        pass

        except:
            break

    if client in subscribers:
        subscribers.remove(client)

    client.close()


PORT = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", PORT))
server.listen()

print(f"Server listening on {PORT}")

while True:

    client, addr = server.accept()

    role = client.recv(1024).decode()

    print(f"{addr} connected as {role}")

    if role == "SUBSCRIBER":
        subscribers.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, role)
    )

    thread.start()