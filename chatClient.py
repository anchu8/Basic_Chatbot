import socket
s = socket.socket()
host = input(str("please enter the host name of the Server:"))
port = 8080
s.connect((host,port))
print("connected to the chat server")
while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Server:", incoming_message)
        print("")
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        
        print("")
    
