from socket import *
import sys

def server():
    sock = socket(family=AF_INET, type=SOCK_STREAM)
    print("SERVER SCOKET CREATE SUCSFULLY")

    sock.bind(("127.0.0.1", int(sys.argv[1])))
    print("SOCKET BINDED TO", sys.argv[1], " PORT")

    sock.listen(2)
    print("IT CAN ACEPT ATMOST 2 ACTIVE CONNECTIONS")

    while True:
        cli, addr = sock.accept()
        print("ACCEPTED", cli, addr)
        #cli.send(b"hello. got your message")
        while True:
            msg = cli.recv(8 * 1024)
            if msg.decode("utf8").strip() == "exit":
                cli.close()
                break
            cli.send(msg.upper())
        #print("RECEIVED MSG FROM CLIENT", msg)


if __name__ == '__main__':
    server()
