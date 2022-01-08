# CONSTANST
from typing import Tuple

BYTE = 1024
KB = 1024 * BYTE
MB = 1024 * KB

def read_file_to_buf(filename: str) -> bytes:
    with open(file=filename, mode="rb") as f:
        return f.read()

def buf_to_file(output_file: str, buf: bytes):
    with open(file=output_file, mode="wb") as f:
        f.write(buf)
        f.flush()

# for server.py
def construct_headers(filename: str, buf: bytes) -> bytes:
    header = f'{filename}\r\n'
    headerByte = bytes(header, encoding='utf-8')
    return headerByte + buf

# for client.py
def decode_headers(buf: bytes) -> Tuple[str, bytes]:
    idx = bytes.find(buf, bytes('\r\n', encoding="utf-8"))
    if idx != -1:
        filename = buf[:idx].decode('utf-8')
        fileBuf = buf[idx+2:]
        return f'receive_{filename}', fileBuf