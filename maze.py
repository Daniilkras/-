from pygame import *
win_width = 700
win_height = 500


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image =transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP]and self.rect.y >5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < win_height + 80:
            self.rect.y += self.speed

class Monster (GameSprite):
    display = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'ringht'
        if self .rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x  -= self.speed
        else:
            self.rect.x += self.speed


class Mall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface ((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



window  =  display.set_mode((700,500))
display.set_caption('Догонялки')
speed = 5
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
bg = transform.scale(image.load('background.jpg'),(700,500))
player = Player('hero.png', 5, win_height - 80, 4)
monster = Monster('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Mall(0,0,0,100,20,450,10)
w2 = Mall(0,0,0,100,480,350,10)
w3 = Mall(0,0,0,100,20,10,300)
w4 = Mall(0,0,0,200,120,10,450)
w5 = Mall(0,0,0,200,120,350,10)
w6 = Mall(0,0,0,450,120,10,450)
w7 = Mall(0,0,0,450,110,10,450)
w8 = Mall(0,0,0,250,120,350,10)
w9 = Mall(0,0,0,180,120,350,10)
font.init()
font = font.Font(None,70)
win = font.render('КРАСАВЧИК',True,(255,215,0))
lose = font.render('ЛОШАРА', True,(180,0,0) )
game = True
finish = False
while game:
 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg,(0,0))
        player.update()
        monster.update()
        monster.reset()
        final.reset()
        player.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
    if sprite.collide_rect(player,monster)or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9):
        finish = True
        window.blit(lose,(200,200))
        kick.play()
    if sprite.collide_rect(player,final):
        finish = True
        window.blit(win,(200,200))
        money.play()
    display.update()
    clock.tick(FPS)