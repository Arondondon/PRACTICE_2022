from tempfile import mkstemp
from os import close
from shutil import move
import time

def write_lines(file):
    T = time.time()
    ft, temp = mkstemp()
    lines = []
    with open(temp, 'w') as t, open(file) as f:
        for line in f:
            if line not in lines:
                lines.append(line)
                t.write(line)
    close(ft)
    move(temp, file)
    T = time.time() - T
    print(f"Program running time is {T} seconds")


if __name__ == '__main__':
    write_lines(file="urls.txt")


