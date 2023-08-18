import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 80))
server_socket.listen(1)

print("Sunucu başlatıldı. İstemci bekleniyor...")

client_socket, client_address = server_socket.accept()
print(f"{client_address} bağlandı.")

while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message == "exit":
        break
    print(f"İstemci: {message}")
    
    response = input("Cevap: ")
    client_socket.send(response.encode("utf-8"))

client_socket.close()
server_socket.close()
