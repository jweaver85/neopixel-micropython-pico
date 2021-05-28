from utils import translate, walk, randColor, render

def color_walk(options):
    # inital state if buffer has been cleared pick two random colors
    if len(options.buffer) == 0:
        walk(randColor(), randColor(), options)

    popped = options.buffer.pop()
    options.colors.push(popped)
    
    # we just popped the last color, walk to another
    if len(options.buffer) == 1:
        walk(popped, randColor(), options)
    
    render(options)
