import pygame as pg, time, random

pg.init()
screen = pg.display.set_mode([600, 600])
pg.display.set_caption('Snake')
running = True
over = False

w, h = 30, 30
x, y = 30, 30
leye, reye = [], []

apple = 0
length = 1
snake = [[x, y]]
direction = 0
delay = 0


def genrandom():
    a = random.randint(0, 600)
    a = a - (a % 30)
    return a


def borderCheck(z):
    if z < 0: return 570
    elif z > 570: return 0
    else: return z


while running:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and direction != 1:
                direction = 0

            if event.key == pg.K_UP and direction != 0:
                direction = 1

            if event.key == pg.K_RIGHT and direction != 3:
                direction = 2
            
            if event.key == pg.K_LEFT and direction != 2:
                direction = 3

    if apple < 1:
        a, b = genrandom(), genrandom()            
        apple += 1
    else:
        pg.draw.rect(screen, "red", (a, b, w, h))

    if delay == 100 and not over:
        if direction == 0:
            y += w
            leye, reye = [5, 20], [18, 20]
        elif direction == 1:
            y -= w
            leye, reye = [5, 5], [18, 5]
        elif direction == 2:    
            x += w
            leye, reye = [20, 5], [20, 18]    
        elif direction == 3:
            x -= w
            leye, reye = [5, 5], [5, 18]  

        delay = 0
        screen.fill("black")

        for i in range(length):
            if snake[i] == [a, b]:
                length += 1
                apple = 0

        x, y = borderCheck(x), borderCheck(y)

        if [x, y] not in snake:
            snake.append([x, y])
            if len(snake) > length:
                snake = snake[1:]
            while len(snake) < length:
                snake.append([x, y])
        else:
            over = True

        for i in range(length):
            pg.draw.rect(screen, "green", (snake[i][0], snake[i][1], w, h))
            
        pg.draw.rect(screen, "red", ((snake[-1][0] + leye[0], snake[-1][1] + leye[1], 8, 8))) # up and down (+5, +20) (+18, +20)
        pg.draw.rect(screen, "red", ((snake[-1][0] + reye[0], snake[-1][1] + reye[1], 8, 8)))

    delay += 1

    pg.display.flip()
    pg.display.update()

pg.quit()