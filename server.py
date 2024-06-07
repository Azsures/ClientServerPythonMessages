import socket
import threading
import sys

def client_handle(conn, addr, list_of_socks):
    while True:
        data = conn.recv(1024).decode('utf8') #traduzir do modo binario para string
        if not data or data.find('||') == -1: #checa se a conexao terminou
            break
        message = data.split('||')[0]  #separa payload do header
        dest_socket = data.split('||')[1].split(':') #separa payload do header

        print(f"\nReceived message: {message}\nDestination: {dest_socket[0]}:{dest_socket[1]}")


        for sockt in list_of_socks:
            if sockt[1][0] == dest_socket[0] and sockt[1][1] == int(dest_socket[1]):
                sockt[0].send(message.encode('utf8'))

            
    
def serve():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 35567
    list_of_sockets = []

    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT)) #fixa o socket do servidor

    sock.listen(10) #permite que ate 10 clients conectem automaticamente
    while True:
        conn, addr = sock.accept() #checa se tem novas conexoes
        list_of_sockets.append([conn, addr]) #caso tenha nova conexao, ele coloca o handle e o socket na lista list_of_sockets
        threading.Thread(target=client_handle, args=(conn, addr, list_of_sockets)).start()


if __name__ == "__main__":
    serve()