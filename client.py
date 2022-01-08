#!/usr/bin/env python3

from time import sleep
from socket import socket, AF_INET, SOCK_STREAM
from config import HOST, PORT
from utils import BYTE, buf_to_file

OUTPUT_RECEIVED_FILE="output.png"

def main():
    with socket(AF_INET, SOCK_STREAM) as s:       
        s.connect((HOST, PORT))

        s.sendall(b'f')

        fileBytes: bytes = b''
        while True:
            try:
                data = s.recv(BYTE)
                fileBytes += data
            except ConnectionResetError as e:
                break
        # save to file
        buf_to_file(OUTPUT_RECEIVED_FILE, fileBytes)

if __name__ == '__main__':
    while True:
        try:
            main()
            break
        except ConnectionRefusedError:
            print("waiting server..., retry in 1sec")
            sleep(1)
