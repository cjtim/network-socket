

# CONSTANST
BYTE = 1024
KB = 1024 * BYTE
MB = 1024 * KB

def read_file_to_buf(filename: str) -> bytes:
    fileByte: bytes
    with open(file=filename, mode="rb") as f:
        fileByte = f.read()
    return fileByte

def buf_to_file(output_file: str, buf: bytes):
    with open(file=output_file, mode="wb") as f:
        f.write(buf)
        f.flush()