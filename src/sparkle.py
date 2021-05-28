from utils import translate, render, randColor


def sparkle(options):
    while len(options.colors) < options.num_pixels:
        options.colors.push(randColor())

    i = 0
    step = options.step
    for c in options.colors:
        if c == (0, 0, 0):
            options.colors[i] = randColor()
        else:
            c1 = translate(c[0], 0, step)
            c2 = translate(c[1], 0, step)
            c3 = translate(c[2], 0, step)
            options.colors[i] = (c1, c2, c3)
        options.pixels.update(i, options.colors[i])
        i = i + 1
    options.pixels.write()

