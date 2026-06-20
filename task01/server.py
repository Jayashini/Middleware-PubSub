import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python server.py <PORT>")
    sys.exit()

PORT = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", PORT))
server.listen(5)

print(f"Server listening on port {PORT}")

client_socket, addr = server.accept()
print(f"Connected by {addr}")

while True:
    message = client_socket.recv(1024).decode()

    if not message:
        break

    print(f"Client: {message}")

client_socket.close()
server.close()