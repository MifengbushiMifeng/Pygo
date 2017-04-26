# !/usr/bin/env python
# encoding=utf-8
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


for n in fab(5):
    print n


def read_file(file_path):
    BLOCK_SIZE = 1024
    with open(file_path, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
