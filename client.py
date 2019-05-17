import socket

def main():
    host = "127.0.0.1"
    port = 8000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    data = s.recv(1024)
    print(data.decode('utf-8'))
    message = input("->  ")
    #while message != 'q':
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)
    print("received from server: "+data.decode('utf-8'))
    #message = input("-> ")
    s.close()

main()

