from pygame import *
from random import randint, choice
window = display.set_mode((1200, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("ffonn.jpg"), (1200, 500))
clock = time.Clock()
font.init()
font2 = font.SysFont("Arial", 100)

win_text = font2.render('Player 1 WIN', True, (255, 215, 0))
lose_text = font2.render('Player 2 WIN', True, (255, 215, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, scale,  player_image, player_x, player_y, player_speed, player_speedx):
        super().__init__()
        self.scale = scale
        self.image = transform.scale(image.load(player_image), (self.scale))
        self.speed = player_speed
        self.speedx = player_speedx
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
        


class Player(GameSprite):
    def update_l(self, number):
        
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0 + number:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 480 - number:
            self.rect.y += self.speed
    def update_r(self, number):
        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0 + number:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 480 - number:
            self.rect.y += self.speed
        
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):
    def update(self):
        if self.rect.y >= 450 or self.rect.y <= 0:
            self.speed *= -1.01
            

        self.rect.y += self.speed
        self.rect.x += self.speedx
        
        

        
        
            
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



FPS = 80
game = True
ball = Enemy((20,20), 'sfera.png', randint(400,600), randint(50,450), choice([2, -2]), choice([2, -2]))
#player = Player((20,100), 'bat3.png', 1100, 420, 12, 1)
#player2 = Player((20,100), 'bat3.png', 50, 420, 12, 2)

slice1player1 = Player((20,20), 'player1.png', 1100, 420, 20, 1)
slice2player1 = Player((20,20), 'player1.png', 1100, 400, 20, 1)
slice3player1 = Player((20,20), 'player1.png', 1100, 380, 20, 1)
slice4player1 = Player((20,20), 'player1.png', 1100, 360, 20, 1)
slice5player1 = Player((20,20), 'player1.png', 1100, 340, 20, 1)
slice1player2 = Player((20,20), 'player2.png', 50, 420, 20, 2)
slice2player2 = Player((20,20), 'player2.png', 50, 400, 20, 2)
slice3player2 = Player((20,20), 'player2.png', 50, 380, 20, 2)
slice4player2 = Player((20,20), 'player2.png', 50, 360, 20, 2)
slice5player2 = Player((20,20), 'player2.png', 50, 340, 20, 2)

while game:
   
    window.blit(background, (0, 0))
    #if sprite.collide_rect(player, ball):
    #            ball.speedx *= -1.2
    #             
    #                
    #if sprite.collide_rect(player2, ball):
    #            ball.speedx *= -1.2 

    if sprite.collide_rect(slice1player1, ball):
        ball.speedx *= -1.2 
        ball.speed *= -1.2 
    if sprite.collide_rect(slice2player1, ball):
        ball.speedx *= -1.4 
        ball.speed *= -1.05
    if sprite.collide_rect(slice3player1, ball):
        ball.speedx *= -1.5 
    if sprite.collide_rect(slice4player1, ball):
        ball.speedx *= -1.4 
        ball.speed *= -1.05
    if sprite.collide_rect(slice5player1, ball):
        ball.speedx *= -1.2 
        ball.speed *= -1.2 


    if sprite.collide_rect(slice1player2, ball):
        ball.speedx *= -1.2 
        ball.speed *= -1.2
    if sprite.collide_rect(slice2player2, ball):
        ball.speedx *= -1.4 
        ball.speed *= -1.05
    if sprite.collide_rect(slice3player2, ball):
        ball.speedx *= -1.5
    if sprite.collide_rect(slice4player2, ball):
        ball.speedx *= -1.4 
        ball.speed *= -1.05
    if sprite.collide_rect(slice5player2, ball):
        ball.speedx *= -1.2 
        ball.speed *= -1.2





                
    if ball.rect.x <= 0:
        window.blit(win_text, (200, 200))
    if ball.rect.x >= 1200:
        window.blit(lose_text, (200, 200))

            
    
    clock.tick(FPS)
    
    
    slice1player1.update_l(80)
    slice2player1.update_l(60)
    slice3player1.update_l(40)
    slice4player1.update_l(20)
    slice5player1.update_l(0)

    slice1player2.update_r(80)
    slice2player2.update_r(60)
    slice3player2.update_r(40)
    slice4player2.update_r(20)
    slice5player2.update_r(0)

    slice1player1.reset()
    slice2player1.reset()
    slice3player1.reset()
    slice4player1.reset()
    slice5player1.reset()
    slice1player2.reset()
    slice2player2.reset()
    slice3player2.reset()
    slice4player2.reset()
    slice5player2.reset()

    #player.update_l()
    #player2.update_r()
    #player.reset()
    #player2.reset()
    ball.update()
    ball.reset()


    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key ==  K_SPACE:
                player.fire()
                

    display.update()
