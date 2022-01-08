#!/usr/bin/env python3

import socket
from config import HOST, PORT
from utils import KB, read_file_to_buf, MB, BYTE
from math import ceil

# instruction
# 1. open connection
# 2. send size to client
# 3. send file to client
# 4. close connection
# 

FILE_TO_SEND = "test_file.png"

def main():
    fileBytes = read_file_to_buf(FILE_TO_SEND)
    size = len(fileBytes)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        # start listen connection
        s.listen() 
        # Wait for an incoming connection
        conn, addr = s.accept()
        with conn:
            print('Receive ping for size in MB from', addr)
            sizeInMB = ceil(size / MB)
            respMB = int.to_bytes(sizeInMB, byteorder='big', length=BYTE)
            conn.sendall(respMB)

        conn, addr = s.accept()
        with conn:
            print('Sending file to', addr)
            # conn.sendfile(open(FILE_TO_SEND, 'rb'))
            conn.sendall(fileBytes)

if __name__ == '__main__':
    main()