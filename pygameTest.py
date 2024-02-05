import pygame
from network import Network

width = 1000
height = 1000 

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Client')

clientNumber = 0

class Player:
    def __init__(self, x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel 


        self.update()    
    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)  

#this code is use to read the positions, and use it in the function to move the tiles      
def read_pos(str):
    #print("String is:", str)
    postions = str.split(",")
    print(f'Postions are {postions} and the type is {type(postions[0])}')
    return (int(postions[0]),int(postions[1]) )

#this is used to send the positions
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])   


def redrawWindow(win,player,player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.get_pos())
    p = Player(startPos[0],startPos[1],100,100,(10,255,125))
    p2 = Player(0,0,100,100,(255,110,11))
    while run:
        p2Pos = read_pos(n.send(make_pos((p.x,p.y)))) #sending the positions of player 1, they are send as string to the server and read as integers for the p2
        p2.x,p2.y = p2Pos
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2)     
main()           




