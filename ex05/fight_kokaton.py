from calendar import c
import pygame as pg
import sys
from random import randint
from pygame import mixer
import tkinter.messagebox as tkm
import time

class Screen:
    
    def __init__(self, title, size, bgi):
        self.title = title
        self.size = size
        self.bgimg = bgi
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgi)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) # 練習3


class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}
    def __init__(self, img, zoom, xy):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                # 練習7
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)
        

class Bomb:
    
    def __init__(self, color, rad, vxy, zoom, scr:Screen):
        self.sfc = pg.Surface((rad*2, rad*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (rad, rad), rad) # 円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        # 練習6
        self.vx, self.vy = vxy
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) # 練習6
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class animal:
    
    def __init__(self, img, zoom, target:Bird, scr):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = (randint(0, scr.rct.width), randint(0, scr.rct.height))
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

class sound:
    def __init__(self, file, times):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play(times)
        
class trap:
    def __init__(self, img, zoom, target:Bird, scr):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = (randint(0, scr.rct.width), randint(0, scr.rct.height))
        
    def update(self, scr:Screen):
       self.rct.center = (randint(0, scr.rct.width), randint(0, scr.rct.height))
        
def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

        
def main():
    scr = Screen("負けるな!こうかとん", (1600, 900), "fig/pg_bg.jpg")
                 
    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb((255, 0, 0), 10, (+1, +1), 1.0, scr)
    
    ani = animal("fig/hitsuji.jpg", 0.3, kkt, scr)
    
    gomi = trap("fig/sneaker.png", 1, kkt, scr)
    
    
    clock = pg.time.Clock() # 練習1
    tm = 0
    while True:
        scr.blit() # 練習2
        ani.blit(scr)
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
            
        kkt.update(scr)

        # 練習7
        bkd.update(scr)
        if tm%100 == 0:
            gomi.update(scr)
        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return
        if kkt.rct.colliderect(ani.rct):
            mee = sound("fig/mee.mp3", 1)
            
        if kkt.rct.colliderect(gomi.rct):
            time.sleep(1)
        
        pg.display.update() #練習2
        clock.tick(1000)
        tm +=1
        
if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()