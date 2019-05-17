import socket
from _thread import *


result =0.0

def client_thread(conn):
    while True:
        while True:
            data = conn.recv(1024)
            val1= data.decode('utf-8')
            conn.sendall(val1.encode('utf-8'))
            op = conn.recv(1024)
            opr = op.decode('utf-8')
            conn.sendall(opr.encode('utf-8'))
            data2 = conn.recv(1024)
            val3 = data2.decode('utf-8')


            if opr == "/":
                result = float(val1)/float(val3)
            elif opr == "+":
                result = float(val1)+float(val3)
            elif opr == "-":
                result = float(val1)-float(val3)
            elif opr == "*":
                result = float(val1)*float(val3)
            res= str(result)
            conn.sendall(res.encode('utf-8'))

    conn.close()


def main():
    host = "127.0.0.1"
    port = 8000
    client_max = 20

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(client_max)
    print ("Listening........")
    c = [client_max]
    addr = [client_max]
    client_count = 0
    while client_count<client_max:
        c, addr= s.accept()
        print("Connected Client " + str(addr))
        start_new_thread(client_thread,(c,))
        client_count+=1
main()
