import socket
from Core.request import Request
from Core.router import Router

class Server:

    def __init__(self,port, environment):
        self.port = port
        self.environment = environment

        self.server = None
        

    def run(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.server.bind(('0.0.0.0', self.port))
        self.server.listen()

        while True:
            client, address = self.server.accept()

            client_request = client.recv(4096).decode()

            #parser requests
            request = Request(client_request)
            request.parse()

            #send request and get response
            router = Router(request.route, request.method, self.environment,request)
            response = router.dispatch()

            #response
            client.send(response.encode())
            client.close()