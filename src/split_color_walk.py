from utils import translate, walk, randColor, render

def split_color_walk(options):
    # inital state if buffer has been cleared pick two random colors
    if len(options.buffer) == 0:
        walk(randColor(), randColor(), options)

    start = int(0) 
    left_middle = int(len(options.colors)/2 - 1)
    right_middle = int(left_middle + 1)
    end = int(len(options.colors) - 1)
    
    popped = options.buffer.pop()
    
    options.colors.remove(start)
    options.colors.insert(left_middle, popped)
    
    options.colors.remove(end)
    options.colors.insert(right_middle, popped)
    
    # we just popped the last color, walk to another
    if len(options.buffer) == 1:
        walk(popped, randColor(), options)
    
    render(options)
    

