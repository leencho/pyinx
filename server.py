import socket
import subprocess
import json
import re


ADDRESS, PORT = ("127.0.0.1", 8000)

request={}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen()
print(f"listening on: {ADDRESS}:{PORT}")
fd, cleint = server.accept()
print("the discriptor", cleint)

def get_request():
    assert False, "NOT implemented GET"
def unsupported_http_version():
    print("==========================================")
    print("Unsported HTTP version                  ")
    print("We only support HTTP version 1.0 and 1.1")
    print("For now we do not support HTTP/1.2      ")
    print("but in the future we might!             ")
    print("Thank you for understanding!            ")
    print("==========================================")
    exit(-1)


while True:
    data = fd.recv(1024)
    recv_len=len(data)
    data = data.decode().strip().split(' ')
    request= {'method':data[0], 'path': data[1], 'version': data[2]}
    print(request)
    if request['version'] != "HTTP/1.0" or request['version'] != "HTTP/1.1":
        print(request['version'])
        unsupported_http_version()
 
    elif  request['method'] =="GET":
        get_request()
    elif request['method'] == "POST":
        assert False, "NOT implemented POST"
    elif request['method']=="PUT":
       assert False, "NOT implemented PUT"
    elif request['method']=='DELETE':
        assert False, "NOT implemented DELETE"
    else:
        print("NOT VALID http")

