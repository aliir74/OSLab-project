import os, sys

# file descriptors r, w for reading and writing
r, w = os.pipe()

processid = os.fork()
if processid:
    # This is the parent process
    os.close(r)
    w = os.fdopen(w, 'w')
    print ("Parent writing")
    w.write("Hello World")
    w.close()
    print ("Parent closing")
    sys.exit(0)
else:
    # This is the child process
    # Closes file descriptor w
    os.close(w)
    r = os.fdopen(r)
    print ("Child reading")
    str = r.read()
    print ("text =", str   )
    sys.exit(0)