from button import Buttons
import pygame as pg

pg.init()



screen = pg.display.set_mode((2000, 800))
flag = True
clock = pg.time.Clock()
while flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
    button1 = Buttons("I hope you are having a blessed day",screen, x_pos=420, y_pos=420, borders=True, text_size=10)
    button2 = Buttons("asdasda",screen, x_pos=420, y_pos=500, text_shadow=True, aliases=False)
    if button1.check_click() or button2.check_click():
        flag = False

    button2.draw()
    button1.draw()
    pg.display.update()
    clock.tick(60)

