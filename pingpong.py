from pygame import *
w_l  = 700
w_w  = 500
wind = display.set_mode((w_l,w_w))
display.set_caption('Ping-Pong')
wind.fill((0,0,255))
game = True
font.init()
font1 = font.Font(None,50)
rect = Rect(0,0,15,65)
class GameSprite(sprite.Sprite):
    def __init__(self,player_x,player_y,player_speed,player_l=15,player_w=65):
        super().__init__()
        self.speed = player_speed
        self.rect =Rect(player_x,player_y,player_l,player_w)
    def reset(self):
        draw.rect(wind,(0,125,225),self.rect)
class Player(GameSprite):
    def __init__(self,player_x,player_y,player_speed,KUP,KDOWN,player_l=15,player_w=65):
        super().__init__(player_x,player_y,player_speed,player_l,player_w)
        self.KUP = KUP
        self.KDOWN = KDOWN
    def move(self):
        keys_press = key.get_pressed()
        if keys_press[self.KUP] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys_press[self.KDOWN] and self.rect.y<w_w-80:
            self.rect.y +=self.speed
racket1 = Player(50,0,1,K_w,K_s)
racket2 = Player(w_l-50,0,1,K_UP,K_DOWN)
while game:
    wind.fill((0,0,255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.move()
    racket2.move()
    racket1.reset()
    racket2.reset()
    display.update()


    
