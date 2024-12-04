import socket
import sys
import time
s = socket.socket()
host = socket.gethostname()
print("Server will start on Host!", host)
port = 8080
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connection")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected to the server and is now online....")
print("")

while 1:
        message1 = input("Welcome to the Chatbot! Type 'exit' or 'quit' to end the chat.")
        ui = input("You: ").lower()
        message1 = message1.encode()
        conn.send(message1)

        message2 = input("Hi, Can I know your name please??")
        message2 = message2.encode()
       
        message3 = input("Hello Anchana! How can I help you??")
        message3 = message3.encode()
       
        print("")
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()

        if (incoming_message == "Hello"):
                print("Chatbot:", message2)
                conn.send(message2)

        elif (incoming_message == "My name is Anchana"):
                print("Chatbot:", message3)
                conn.send(message3)
        print("")
