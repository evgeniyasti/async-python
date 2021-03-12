# Echo server program
import socket
import time


def echo_server():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 8080              # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024).decode("utf-8")
                    received = "Received {received}".format(received=data)
                    time.sleep(1)
                    conn.sendall(bytes(received, "utf-8"))
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    while True:
        echo_server()