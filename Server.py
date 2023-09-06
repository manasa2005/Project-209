import socket
from  threading import Thread
import time
import os

import socket
from  threading import Thread
import time
import os

SERVER = None
PORT = 12345
IP_ADDRESS = '127.0.0.1'
Clients = {}

def setup():
    global SERVER, PORT, IP_ADDRESS
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP_ADDRESS, PORT))
    server.listen(100)
    print(f"Server is listening on {IP_ADDRESS}:{PORT}")

def acceptConnection():
    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")
        # Handle the client connection and save client information (e.g., create a new thread)

def main():
    setup()
    acceptConnection()

if __name__ == "__main__":
    main()
