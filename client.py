#!/usr/bin/env python3

import socket
from config import HOST, PORT
from utils import BYTE, buf_to_file

OUTPUT_RECEIVED_FILE="output.png"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'f')

        fileBytes: bytes = b''
        while True:
            try:
                data = s.recv(BYTE)
                fileBytes += data
            except ConnectionResetError as e:
                break
        buf_to_file(OUTPUT_RECEIVED_FILE, fileBytes)

if __name__ == '__main__':
    main()