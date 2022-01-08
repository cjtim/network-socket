#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from config import HOST, PORT
from utils import construct_headers, read_file_to_buf

# instruction
# 1. open connection
# 2. send size to client
# 3. send file to client
# 4. close connection
# 

def main():
    FILE_TO_SEND = input('input path of file: ')
    fileBytes = read_file_to_buf(FILE_TO_SEND)
    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        # start listen connection
        s.listen() 
        print('wait for client.py...')
        # Wait for an incoming connection
        conn, addr = s.accept()
        with conn:
            print('Sending file to', addr)
            # conn.sendfile(open(FILE_TO_SEND, 'rb'))
            conn.sendall(construct_headers(FILE_TO_SEND, fileBytes))

if __name__ == '__main__':
    main()