import socket
import threading
import sys

def client_handle(conn, addr):
    data = conn.recv(1024).decode('utf8')
    message = data.split('||')[0]
    dest_socket = data.split('||')[1].split(':')
    print(f"\nReceived message: {message}\nDestination: {dest_socket[0]}:{dest_socket[1]}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((dest_socket[0], int(dest_socket[1])))
            s.send(message.encode('utf8'))
            if(s.recv(1024).decode('utf8') == "sucess"):
                conn.send(b"Sucess")
    except:
        conn.send(b"error connecting to destination")
        print("error connecting")
    
def serve():
    HOST = "192.168.88.62"
    PORT = 36890

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((HOST,0))
            sock.listen(2)
            while True:
                print(f"\nPre Active Threads: {threading.active_count()}")
                conn, addr = sock.accept()
                threading.Thread(target=client_handle, args=(conn, addr)).start()
                print(f"\nActive Threads: {threading.active_count()}")
    except Exception as ex:
        print(ex)
    except KeyboardInterrupt as ex:
        print(ex)
    except:
        print(sys.exec_info())

if __name__ == "__main__":
    serve()