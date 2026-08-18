import zlib

def compress_decompress():
    text = "Hello World! Hello World! Hello World! Hello World!"

    compressed = zlib.compress(text.encode())
    print(compressed)

    decompressed = zlib.decompress(compressed).decode()
    print(decompressed)

compress_decompress()