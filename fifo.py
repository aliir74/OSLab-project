import os, time, sys
pipe_name = 'pipe_test'

def child( ):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
#    while True:
 #       time.sleep(1)
    os.write(pipeout, 'hello world\n')

def parent( ):
    pipein = open(pipe_name, 'r')
    #while True:
    line = pipein.readline()[:-1]
    print line

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)  
pid = os.fork()    
if pid != 0:
    parent()
else:       
    child()


