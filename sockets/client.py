from socket import *
import sys

def client():
    sock = socket(family=AF_INET, type=SOCK_STREAM)
    print("SERVER SCOKET CREATE SUCSFULLY")
    

    sock.bind(("127.0.0.1", int(sys.argv[1])))

    sock.connect(("127.0.0.1", 5000))

    msg = input()
    sock.send(msg.encode())
    rcvmsg= sock.recv(1024)
    print(rcvmsg)
    sock.send(b"exit")
        
    sock.close()

if __name__ == '__main__':
    client()
