import os, time, sys
import sysv_ipc
pipe_name = 'pipe_test'

def child( ):
	while 1:
		t = mq.receive()
		print(t)
def parent( ):
	mq.send('hello world')

mq = sysv_ipc.MessageQueue(None, flags= sysv_ipc.IPC_CREAT | sysv_ipc.IPC_EXCL)
pid = os.fork()    
if pid != 0:
    parent()
else:       
    child()


