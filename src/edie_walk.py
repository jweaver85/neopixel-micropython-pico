from utils import translate, walk, render

RED = (0,255,0)
WHITE = (0,125,184)
BLUE = (190,51,214)

def edie_walk(options):
    if len(options.buffer) == 0:
        walk(RED, WHITE, options)
        walk(WHITE, BLUE, options)
        walk(BLUE, WHITE, options)
        walk(WHITE, RED, options)

    popped = options.buffer.pop()
    options.colors.push(popped)
    options.buffer.push(popped)
    
    render(options)

