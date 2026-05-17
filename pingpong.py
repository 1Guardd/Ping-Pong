from pygame import *
w_l  = 700
w_w  = 500
wind = display.set_mode((w_l,w_w))
display.set_caption('Ping-Pong')
wind.fill((0,0,255))
game = True
font.init()
font1 = font.Font(None,50)
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_l=15,player_w=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_l,player_w))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        wind.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,KUP,KDOWN,player_l=15,player_w=65):
        super().__init__(self,player_image,player_x,player_y,player_speed,player_l,player_w)
        self.KUP = KUP
        self.KDOWN = KDOWN
    def move(self):
        keys_press = key.get_pressed()
        if keys_press[self.KUP] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys_press[self.KDOWN] and self.rect.y<w_w-80:
            self.rect.y +=self.speed



    
