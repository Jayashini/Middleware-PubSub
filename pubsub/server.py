import socket
import threading
import sys

topics = {}
lock = threading.Lock()

def handle_client(client, role, topic):

    try:
        while True:
            message = client.recv(1024).decode()

            if not message:
                break

            print(f"[{topic}] {message}")

            if role == "PUBLISHER":

                with lock:
                    subscribers = topics.get(topic, []).copy()

                for sub in subscribers:
                    try:
                        sub.send(f"[{topic}] {message}".encode())
                    except:
                        pass

    except:
        pass

    finally:

        if role == "SUBSCRIBER":
            with lock:
                if topic in topics and client in topics[topic]:
                    topics[topic].remove(client)

        client.close()


def start_server(port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("0.0.0.0", port))
    server.listen(100)

    print(f"Broker running on port {port}")

    while True:

        client, addr = server.accept()

        try:
            info = client.recv(1024).decode()

            role, topic = info.split("|")

            print(f"{addr} -> {role} -> {topic}")

            if role == "SUBSCRIBER":

                with lock:
                    if topic not in topics:
                        topics[topic] = []

                    topics[topic].append(client)

            thread = threading.Thread(
                target=handle_client,
                args=(client, role, topic),
                daemon=True
            )

            thread.start()

        except:
            client.close()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python server.py <PORT>")
        sys.exit()

    PORT = int(sys.argv[1])

    start_server(PORT)