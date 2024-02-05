import socket
from _thread import *
from player import Player
import pickle


server = "10.0.0.114"
port = 5557

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)
#print("Server started, waiting for connection...")


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]



def threaded_client(conn,player):  #this works asynchronously
    #conn.send(str.encode("Connected"))
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data
            #reply = data.decode("utf-8")

            if not data:
                print("Disconnected...")
                break
            else:
                if player == 1:
                
                    reply = players[0]
                else:
                    reply = players[1]    


                print("Received: ",reply)
                print("Sending: ",reply)
            conn.sendall(pickle.dumps(reply))    
        except:
            print("Something is wrong") 
            break
    print("Lost Connection")
    conn.close()       

currentPlayer = 0
while True:
    conn,addr = s.accept()
    print("Connected to: ",addr)
    start_new_thread(threaded_client,(conn,currentPlayer))
    currentPlayer+=1
