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
    def update_l(self):
        
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y < 450:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 0:
            self.rect.y += self.speed
    def update_r(self):
        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y < 450:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 0:
            self.rect.y += self.speed
        
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):
    def update(self):
        if self.rect.y >= 450 or self.rect.y <= 0:
            self.speed *= -1
        
        self.rect.y += self.speed
        self.rect.x += self.speedx
        
        

        
        
            
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



FPS = 30
game = True
ball = Enemy((50,50), 'sfera.png', randint(400,600), randint(50,450), choice([10, -10]), choice([10, -10]))
player = Player((50,200), 'bat3.png', 1100, 420, 10, 1)
player2 = Player((50,200), 'bat3.png', 50, 420, 10, 2)
while game:
   
    window.blit(background, (0, 0))
    if sprite.collide_rect(player, ball):
                ball.speedx *= -1 
    if sprite.collide_rect(player2, ball):
                ball.speedx *= -1 
                
    if ball.rect.x <= 0:
        window.blit(win_text, (200, 200))
    if ball.rect.x >= 1200:
        window.blit(lose_text, (200, 200))

            
    
    clock.tick(FPS)
    
    
    
    player.update_l()
    player2.update_r()
    player.reset()
    player2.reset()
    ball.update()
    ball.reset()


    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key ==  K_SPACE:
                player.fire()
                

    display.update()
