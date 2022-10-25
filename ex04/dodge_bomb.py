import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode_mode((1600, 900))
    
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rfc = bg_sfc.get_rect()
    
    scrn_sfc.blit(bg_sfc, bg_rfc)
    
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)
    
if __name__ == "__main_":
    pg.init()
    main()
    pg.quit()
    sys.exit()