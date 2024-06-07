import socket
import threading
from time import sleep

HOST = socket.gethostbyname(socket.gethostname())  # The server's IP address
PORT = 35567  # The port used by the server


def send_message(s):
    while True:
        message = input(">> ")
        message = f"{message}||{HOST}:{34560}"
        s.send(message.encode('utf8'))

def receive_message(s):
    while True:
        data = s.recv(1024).decode('utf8')
        print(f"\n<< {data}\n>> ", end="")

s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), 35580))
#s.bind(('10.100.0.85', 35580))
s.connect((HOST, PORT))
receive = threading.Thread(target=receive_message, args=(s,))
receive.start()
send    = threading.Thread(target=send_message, args=(s,))
send.start()
