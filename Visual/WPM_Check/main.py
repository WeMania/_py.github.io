import pygame as pg, time
import colors, functions as fc

pg.init()
WIDTH, HEIGTH = 900, 400
screen = pg.display.set_mode([WIDTH, HEIGTH])
pg.display.set_caption('WPM TEST')

f_size_default = 50
f_size_stat = 64
font_default = pg.font.Font("assets/fonts/FiraMono-Bold.ttf", f_size_default)
font_stat = pg.font.Font("assets/fonts/FiraMono-Bold.ttf", 64)

letters =  "abcdefghijklmnopqrstuvwxyz,.!?'"

running = True
on = True

view = 0
view_start = False

user_text = ""

with open("assets/words.txt", "r") as file:
    text = fc.get_text(file.read())
    file.close()


start_time = time.time()
while running:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:                
            if (event.unicode).lower() in list(letters) or event.key == pg.K_SPACE:
                user_text += event.unicode
                if view_start:
                    view -= 28 
            elif event.key == pg.K_BACKSPACE:
                user_text = user_text[:-1]
                if view_start:
                    view += 28  

    if on:
        x = 28
        y = HEIGTH / 2 - f_size_default

        screen.fill(colors.BACKGROUND)

        for s in text:
            fc.draw_letter(s, colors.DEFAULT, screen, font_default, [x+view, y])
            
            x += 28

        x = 28

        for i, s in enumerate(user_text):
            if s != text[i]:
                pg.draw.rect(screen, colors.BACKGROUND, (x+view, y, 28, 50))
                color = colors.WRONG
            else:
                color = colors.RIGHT
            
            if s == " ":
                fc.draw_letter(text[i], color, screen, font_default, [x+view, y])
            else:
                fc.draw_letter(s, color, screen, font_default, [x+view, y])
            
            x += 28
            if x > 200:
                view_start = True


        loop_time = int(time.time() - start_time)
        if (time.time() - start_time) > 30:
            wpm, percentege = fc.get_wpm(user_text, loop_time), fc.get_pec(user_text, text)

            fc.draw_result(wpm, percentege, screen, font_stat)
            on = False
        else:
            fc.draw_time(str(30 - round(loop_time)), screen, font_stat, [WIDTH, HEIGTH])

    pg.display.flip()
    pg.display.update()

pg.quit()