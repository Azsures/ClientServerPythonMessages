import socket
import threading
import sys

def client_handle(conn, addr, list_of_socks):
    while True:
        data = conn.recv(1024).decode('utf8')
        if not data or data.find('||') == -1:
            break
        message = data.split('||')[0]
        dest_socket = data.split('||')[1].split(':')
        print(f"\nReceived message: {message}\nDestination: {dest_socket[0]}:{dest_socket[1]}")


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            for sockt in list_of_socks:
                print(sockt)
                if sockt[1][0] == dest_socket[0] and sockt[1][1] == int(dest_socket[1]):
                    sockt[0].send(message.encode('utf8'))
            #s.connect((dest_socket[0], int(dest_socket[1])))
            #conn.send(message.encode('utf8'))
            #if(s.recv(1024).decode('utf8') == "sucess"):
                #   conn.send(b"Sucess")

            
    
def serve():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 35567
    list_of_sockets = []

    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    print(HOST, PORT)
    sock.listen(10)
    while True:
        conn, addr = sock.accept()
        list_of_sockets.append([conn, addr])
        threading.Thread(target=client_handle, args=(conn, addr, list_of_sockets)).start()


if __name__ == "__main__":
    serve()