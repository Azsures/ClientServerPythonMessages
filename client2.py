import socket
import threading
from time import sleep

HOST = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 35567  # The port used by the server


def send_message(s):
    while True:
        message = input(">> ")
        message = f"{message}||10.100.0.83:5556"
        s.send(message.encode('utf8'))

def receive_message(s):
    while True:
        data = s.recv(1024).decode('utf8')
        print(f"\n<< {data}\n>> ", end="")



s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), 34560))
s.connect((socket.gethostbyname(socket.gethostname()), 35567))
#s.connect(('10.100.0.83', 5555))
receive = threading.Thread(target=receive_message, args=(s,))
receive.start()
send    = threading.Thread(target=send_message, args=(s,))
send.start()
    