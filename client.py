import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 80))

while True:
    message = input("Mesaj: ")
    client_socket.send(message.encode("utf-8"))
    
    if message == "exit":
        break
    
    response = client_socket.recv(1024).decode("utf-8")
    print(f"Sunucu: {response}")

client_socket.close()

