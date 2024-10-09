import socket
import subprocess
import json
import re


ADDRESS, PORT = ("127.0.0.1", 8000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen()
print(f"listening on: {ADDRESS}:{PORT}")
fd, cleint = server.accept()
print("the discriptor", cleint)
while True:
    data = fd.recv(1024)
    recv_len=len(data)
    if data.startswith(b"GET "):
        assert False, "NOT implemented GET"
    elif data.startswith(b"POST"):
        assert("NOT implemented POST")
    elif data.startswith("PUT"):
       assert("NOT implemented PUT")
    elif data.startswith("DELETE"):
        assert("NOT implemented DELETE")
    else:
        print("NOT VALID http")

    

    print((data.decode().strip()))