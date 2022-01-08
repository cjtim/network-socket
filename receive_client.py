#!/usr/bin/env python3

from time import sleep
from socket import socket, AF_INET, SOCK_STREAM
from config import HOST, PORT
from utils import BYTE, buf_to_file, decode_headers

def main():
    with socket(AF_INET, SOCK_STREAM) as s:       
        s.connect((HOST, PORT))

        s.sendall(b'get me file!')

        fileBytes: bytes = b''
        while True:
            try:
                data = s.recv(BYTE)
                fileBytes += data
            except ConnectionResetError:
                break

        filename, filebyte = decode_headers(fileBytes)
        # save to file
        print(f'saved to {filename}')
        buf_to_file(filename, filebyte)

if __name__ == '__main__':
    while True:
        try:
            main()
            break
        except ConnectionRefusedError:
            print('waiting for server retry in 1sec...')
            sleep(1)
