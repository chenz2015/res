import socket
import sys
import signal
import datetime

addr = ('', 51403)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)

def quit(signum, frame):
    s.close()
    sys.exit()

def writeip(ip):
    print('accepted')
    try:
        f = open('/root/files/ip', 'w')
        f.write(ip+' '+str(datetime.datetime.now()))
        f.close()
    except:
        pass


def fun():
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    while True:
        data, addr = s.recvfrom(2048)
        data = data.decode('utf-8')
        if (data == 'wde23fc59'):
            writeip(addr[0])

fun()

