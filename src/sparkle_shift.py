from utils import translate, render, randColor

RED = (0,255,0)
WHITE = (0,125,184)
BLUE = (190,51,214)

shift_count = 0

def sparkle_shift(options):
    global shift_count
    while len(options.colors) < options.num_pixels:
        options.colors.push(randColor())

    i = 0
    step = 1
    if shift_count == 15:
        options.colors.push(options.colors.pop())
        shift_count = 0
    else:
        shift_count = shift_count + 1

    for c in options.colors:
        if c == (0, 0, 0):
            options.colors[i] = randColor()
        else:
            c1 = translate(c[0], 0, step)
            c2 = translate(c[1], 0, step)
            c3 = translate(c[2], 0, step)
            options.colors[i] = (c1, c2, c3)
        options.pixels[i] = options.colors[i]
        i = i + 1
    options.pixels.write()
