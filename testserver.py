import socket
HEADERSIZE = 10

# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234)) #hostname/portnumber
s.listen(5) # creates a queue

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established.")

    msg = "Welcome to the Server"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg,"utf-8"))
    '''
    clientsocket.send(bytes("Welcome to the Chatroom","utf-8")) # sending data from client
    clientsocket.close()
    '''
