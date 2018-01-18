import mmap
import os

mm = mmap.mmap(-1, 13)


pid = os.fork()

if pid == 0:  # In a child process
    #mm.seek(0)
    print mm.readline()

    mm.close()
else:
    mm.write("Hello world!")
