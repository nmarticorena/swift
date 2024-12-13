from swift import start_servers
from queue import Queue


outq = Queue()
inq = Queue()

def stop_servers():
    return False

start_servers(outq, inq, stop_servers)

while 1:
    pass
