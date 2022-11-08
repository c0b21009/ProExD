import pygame
import sys
import random
import math

img_bg = pygame.image.load("png/BG.png")
img_player = pygame.image.load("png/Plane/01.png")
img_weapon = pygame.image.load("png/Bullet/1.png")
img_enemy = [
    pygame.image.load("png/minion/1.png"),#敵画像
    pygame.image.load("png/ufo.png")#敵の攻撃弾画像
]
WIDTH = 1200
HEIGHT = WIDTH/2
bg_y = 0
px = 320 #プレイヤーのX座標
py = 240 #プレイヤーのY座標
bx = 0 #弾のX座標
by = 0 #弾のY座標
t = 0 #タイマー変数
space = 0
BULLET_MAX = 100 #弾の最大値
ENEMY_MAX = 100 #敵の最大数
bull_n = 0
bull_x =[0]*BULLET_MAX
bull_y =[0]*BULLET_MAX
bull_f =[False]*BULLET_MAX

ebull_n = 0
ebull_x = [0]*ENEMY_MAX
ebull_y = [0]*ENEMY_MAX
ebull_a = [0]*ENEMY_MAX
ebull_f =[False]*ENEMY_MAX
ebull_f2 = [False]*ENEMY_MAX
e_list = [0]*ENEMY_MAX
e_speed = [0]*ENEMY_MAX


def set_bullet():#弾のスタンバイ
    global bull_n
    bull_f[bull_n] = True
    bull_x[bull_n] = px-16
    bull_y[bull_n] = py-32
    bull_n = (bull_n+1)%BULLET_MAX

def move_bullet(screen):#弾を飛ばす
    for i in range(BULLET_MAX):
        if bull_f[i] == True:
            bull_y[i] = bull_y[i] - 32
            screen.blit(img_weapon,[bull_x[i],bull_y[i]])
            if bull_y[i] < 0:
                bull_f[i] = False

def move_player(screen,key):
    global px,py,space
    if key[pygame.K_UP] == 1:
        py = py - 10
        if py < 20:
            py = 20
    if key[pygame.K_DOWN] == 1:
        py = py + 10
        if py > HEIGHT:
            py = HEIGHT
    if key[pygame.K_LEFT] == 1:
        px = px - 10
        if px < 20:
            px = 20
    if key[pygame.K_RIGHT] == 1:
        px = px + 10
        if px > WIDTH:
            px = WIDTH
    space = (space+1)*key[pygame.K_SPACE]
    if space%5 == 1: #5フレーム毎に弾を飛ばす
        set_bullet()

    screen.blit(img_player,[px-16,py-16])
def set_enemy(x,y,a,enemy,speed):
    global ebull_n
    while True:
        if ebull_f[ebull_n] == False:
            ebull_f[ebull_n] = True
            ebull_x[ebull_n] = x
            ebull_y[ebull_n] = y
            ebull_a[ebull_n] = a
            e_list[ebull_n] = enemy
            e_speed[ebull_n] = speed
            break
        ebull_n = (ebull_n+1)%ENEMY_MAX

def move_enemy(screen):
    for i in range(ENEMY_MAX):
        if ebull_f[i] == True:
            png = e_list[i]
            ebull_x[i] = ebull_x[i] + e_speed[i]*math.cos(math.radians(ebull_a[i]))
            ebull_y[i] = ebull_y[i] + e_speed[i]*math.sin(math.radians(ebull_a[i]))
            if e_list[i] == 0 and ebull_y[i] > 100 and ebull_f2[i] == False:#弾を発射
                set_enemy(ebull_x[i],ebull_y[i],90,1,15)
                ebull_f2[i] = True
            if ebull_x[i] < -40 or ebull_x[i] > 680 or ebull_y[i] < -40 or ebull_y[i] > 520:#画面外に敵が消える
                ebull_f[i] = False
                ebull_f2[i] = False
                
            rz = pygame.transform.rotozoom(img_enemy[png],0,1.0)
            screen.blit(rz,[ebull_x[i]-rz.get_width()/2,ebull_y[i]-rz.get_height()/2])

def main():
    global t,bg_y
    pygame.init()
    pygame.display.set_caption("戦えこうかとん")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        print(e_list)
        t=t+1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg_y = (bg_y+16)%HEIGHT
        screen.blit(img_bg,[0,bg_y-HEIGHT])
        screen.blit(img_bg,[0,bg_y])
        key = pygame.key.get_pressed()
        move_player(screen,key)
        move_bullet(screen)
        if t%30 == 0:#30フレームにつき敵1体出現
            set_enemy(random.randint(20,WIDTH),-10,90,0,6)
        move_enemy(screen)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()