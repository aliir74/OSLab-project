import mmap
import os
import time


fw = open("hello.txt", "wb")
fr = open("hello.txt", "r+b")

pid = os.fork()

if pid == 0:  # In a child process
    #mm.seek(0)
    time.sleep(1)
    mm = mmap.mmap(fr.fileno(), 0)
    print mm.readline()

    mm.close()
else:
    fw.write("Hello Python!\n")
