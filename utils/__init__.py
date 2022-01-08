# CONSTANST
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

def get_extension(filename: str) -> str:
    from mimetypes import guess_type, guess_extension
    type, _ = guess_type(filename)
    return guess_extension(type)