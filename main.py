from button import Buttons
import pygame as pg

pg.init()



screen = pg.display.set_mode((1000, 600))
flag = True
clock = pg.time.Clock()
while flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
    button1 = Buttons("text",screen, 50, 50, 100, 50)
    if button1.check_click():
        flag = False


    button1.draw()
    pg.display.update()
    clock.tick(60)

