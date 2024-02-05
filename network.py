import socket
import pickle
class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.port = 5557
        self.server = "10.0.0.114"
        self.addr = (self.server,self.port)
        self.p = self.connect()
        #print(self.id)
    def get_P(self):
        return self.p   

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass
    def send(self,data):
        try:
            #print("Hello: ",data)
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096)) 
        except socket.error as e:
            print(e)  
# n = Network() 
# print(n.send("Hello"))
# print(n.send("World!"))       