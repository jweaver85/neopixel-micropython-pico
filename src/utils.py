import random


def translate(start, end, stepSize):
    if start == end:
        return end
    elif start > end:
        if start-stepSize <= end:
            return end
        else:
            return start-stepSize
    else:
        if start+stepSize >= end:
            return end
        else:
            return start+stepSize


def walk(c1, c2, options):
    while c1 != c2:
        c1 = (
            translate(c1[0], c2[0], options.step),
            translate(c1[1], c2[1], options.step),
            translate(c1[2], c2[2], options.step)
        )
        options.buffer.push(c1)


def render(options):
    i = 0
    for c in options.colors:
        options.pixels.update(i, c)
        i = i+1
    options.pixels.write()


def rand():
    return int(255 * random.random())


def randColor():
    return (rand(), rand(), rand())

