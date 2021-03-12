# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import time
import socket

SMSs = ["sms1", "sms2", "sms3", "sms4", "sms5", "sms6", "sms7"]

async def send_data(sock):
    print("STARTING TO SEND")
    for sms in SMSs:
        #critical section
        sock.sendall(bytes(sms, "utf-8"))
        await asyncio.sleep(0.1)


async def receive_data(sock):
    print("STARTING TO RECEIVE")
    while True:
        print("BLOCK")
        data = sock.recv(1024)
        await asyncio.sleep(0.1)
        data0 = data.decode("utf-8")
        print(data0)
        if data0.find("7") > 0: #sentinel value
            break


async def start_async(PORT):

    HOST = '127.0.0.1'    # The remote host
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        await receive_data(sock)
        await send_data(sock)


if __name__ == '__main__':
    start_time = time.perf_counter()
    PORT = 8080
    asyncio.run(start_async(PORT))
    run_time = time.perf_counter() - start_time
    print(f"Program ran for {run_time:.2f} seconds!")


