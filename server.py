import socket
import subprocess
import json
import re


class Http_server():
    def __init__(self, address="127.0.0.1", port=8000):
        self.address=address
        self.port=port
        self.request = {}
        self.response=""
    def run(self):
        server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.address, self.port))
        server.listen()
        print(f"Listening on {self.address}:{self.port}")
        fd, client= server.accept()
        print(f"received connection from {client}")
        while True:
            self.response={}
            data = fd.recv(1024)
            data=data.decode().strip().split(' ')
            self.request = {"method": data[0], "path": data[1], "version": data[2]}
            if self.request['version'] == "HTTP/1.1" or self.request['version']=='HTTP/1.0':
                if self.request['method']=='GET':
                    self.get_request(fd)
                elif self.request['method']=='POST':
                    self.post_request()
                elif self.request['method']=='PUT':
                    id=0 #must emplement asking for id here
                    self.put_request(id=id)
                elif self.request['method']=='DELETE':
                    id=0
                    self.delete_request(id)
                else:
                    assert False, "NOT valid HTTP request"
            else:
                self.unsupported_http_version()
            

    
    def get_request(self, fd):
        if self.request['path']=='/':
            header=b"HTTP/1.1 200 ok\r\n"
            print(header)
            fd.send(header)
            
        else:
            self.error404()
            

    def post_request(self):
        assert False, "NOT Implemented"
    def put_request(self, id):
        assert False, "NOT Implemented"
    def delete_request(self, id):
        assert False, "NOT Implemented"
    def error404(self):
        assert False, "not Implemented"
    def unsupported_http_version(self):
        print("==========================================")
        print("Unsported HTTP version                  ")
        print("We only support HTTP version 1.0 and 1.1")
        print("For now we do not support HTTP/1.2      ")
        print("but in the future we might!             ")
        print("Thank you for understanding!            ")
        print("==========================================")
        exit(-1)
    





if __name__=="__main__":
    server=Http_server(port=5000)
    server.run()