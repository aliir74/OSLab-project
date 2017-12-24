import os


pipein, pipeout = os.pipe()
if os.fork() == 0:
    #child
else:
    #parent
    os.write()