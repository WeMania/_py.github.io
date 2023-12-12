import pygame as pg, time, random

pg.init()

w, h = 360, 720
screen = pg.display.set_mode([w, h])

running = True
left, right = True, True

color = "red"

sqr = 30

in_shapes = []

gravity = 0
delay = 0
spawn = False


def generate_shape():
    o_block = [[0, 0], [0, sqr], [sqr, sqr], [sqr, 0]]
    l_block = [[0, 0], [sqr, 0], [sqr * 2, 0], [sqr * 3, 0]]
    r_block = [[0, 0], [0, sqr], [0, sqr * 2], [0, sqr * 3]]
    j_block = [[sqr, -sqr], [sqr, 0], [sqr * 2, 0], [sqr * 3, 0]]
    l_block = [[0, 0], [sqr, 0], [sqr * 2, 0], [sqr * 2, -sqr]]
    s_block = [[0, 0], [0, -sqr], [-sqr, -sqr], [-sqr, -sqr * 2]] # [[0, 0], [sqr, 0], [sqr, -sqr], [sqr * 2, -sqr]]
    z_block = [[0, -sqr], [sqr, -sqr], [sqr, 0], [sqr * 2, 0]]
    t_block = [[0, 0], [sqr, 0], [sqr * 2, 0], [sqr, -sqr]]
    blocks = [o_block, l_block, j_block, l_block, s_block, z_block, t_block, r_block]

    block = random.choice(blocks) 
    return block


def rotate_clockwise(x_block):
    for i in range(len(x_block)):
        x_block[i][0] = -(x_block[i][0]) 
        x_block[i].reverse()

    return x_block


def rotate_counter_clockwise(y_block):
    for i in range(len(y_block)):
        y_block[i][1] = -(y_block[i][1]) 
        y_block[i].reverse()

    return y_block


def add_shapes(x_shape, y_coord):
    for i, c in enumerate(x_shape):
        c[0] += y_coord[i][0]
        c[1] += y_coord[i][1]

        in_shapes.append(c)


def gravity(y):
    for i in range(len(in_shapes)):
        if in_shapes[i][1] < y:
            in_shapes[i][1] += 30


def remove_y(y):
    global in_shapes
    num = 0

    while num < len(in_shapes):
        if in_shapes[num][1] == y:
            in_shapes.remove(in_shapes[num])
        else:
            num += 1


def count_cords(cords):
    global w, h, sqr
    width = 0
    for i in range(int(h / sqr) + 1):
        for j in range(int(h / sqr) + 1):
            if [j * sqr, i * sqr] in cords:
                width += 1
                if width == int(w / sqr):
                    remove_y(i * sqr)
                    gravity(i * sqr)
            else:
                width = 0
                break


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                coord = rotate_clockwise(coord)

            if event.key == pg.K_a:
                coord = rotate_counter_clockwise(coord)

            for cord in shape:
                if event.key == pg.K_RIGHT and right:
                    cord[0] += sqr
            
                if event.key == pg.K_LEFT and left:
                    cord[0] -= sqr
    
    screen.fill("black")
    left, right = True, True

    if spawn:
        for i, z in enumerate(shape):
            if not spawn:
                break

            x, y = z[0] + coord[i][0], z[1] + coord[i][1]

            pg.draw.rect(screen, "green", (x, y, sqr, sqr))
            
            if y == h - sqr:
                add_shapes(shape, coord)
                spawn = False
                break

            if x + sqr == w:
                right = False
            if  x == 0:
                left = False
            if x < 0:
                for u in shape:
                    u[0] += 30
            if x > w - sqr:
                for u in shape:
                    u[0] -= 30

            for q in in_shapes:
                if q[1] == sqr:
                    running = False
                
                if q[1] == y + sqr and q[0] == x:
                    add_shapes(shape, coord)
                    spawn = False
                    break

                if q[1] == y:
                    if q[0] == x + sqr:
                        right = False
                    if q[0] == x - sqr:
                        left = False

    if not spawn:
        shape = [[0, 0], [0, 0], [0, 0], [0, 0]]
        coord = generate_shape()
        for square in shape:
            square[0] += 150
        spawn = True

    if delay == 150:
        for cords in shape:
            cords[1] += sqr
        delay = 0
        count_cords(in_shapes)

    for s in in_shapes:
        pg.draw.rect(screen, "green", (s[0], s[1], sqr, sqr))

    delay += 1
    pg.display.flip()
    pg.display.update()

pg.quit()