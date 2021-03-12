# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import time

SMSs = ["sms1", "sms2", "sms3", "sms4", "sms5", "sms6", "sms7"]


def client_sequential(PORT):
    import socket

    HOST = '127.0.0.1'    # The remote host
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        for sms in SMSs:
            send(sock, sms)
            receive(sock)

def receive(s):
    data = s.recv(1024)
    print(data.decode("utf-8"))

def send(s, sms):
    s.sendall(bytes(sms, "utf-8"))
    print("Sending {sms}".format(sms=sms))


if __name__ == '__main__':
    start_time = time.perf_counter()
    PORT = 8080
    client_sequential(PORT)
    run_time = time.perf_counter() - start_time
    print(f"Program ran for {run_time:.2f} seconds!")


