import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

for i in range(0,100):
    conn.sendall("YEEAAHHHHH BAABYYYYYY!!!!!!")
    data = conn.recv(1024)
    print("Rec:",data)