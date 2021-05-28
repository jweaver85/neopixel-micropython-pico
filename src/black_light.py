from utils import translate, walk, render

COLOR01 = (171,103,164)
COLOR02 = (121,132,160)
COLOR03 = (105,135,156)
COLOR04 = (203,53,98)
COLOR05 = (168,62,184)

colors = [COLOR01, COLOR02, COLOR03, COLOR04, COLOR05]

def black_light(options):
    if len(options.buffer) < 60:
        walk(COLOR01, COLOR02, options)
        walk(COLOR02, COLOR03, options)
        walk(COLOR03, COLOR04, options)
        walk(COLOR04, COLOR05, options)
        walk(COLOR05, COLOR01, options)

    popped = options.buffer.pop()
    options.colors.push(popped)
    options.buffer.push(popped)
    render(options)
