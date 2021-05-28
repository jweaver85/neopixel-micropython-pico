from utils import translate, walk, render

RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

def rand():
    return int(255 * random.random())

def split_america_walk(options):
    if len(options.buffer) == 0:
        walk(RED, WHITE, options)
        walk(WHITE, BLUE, options)
        walk(BLUE, WHITE, options)
        walk(WHITE, RED, options)
     
    start = int(0) 
    left_middle = int(len(options.colors)/2 - 1)
    right_middle = int(left_middle + 1)
    end = int(len(options.colors) - 1)
    
    popped = options.buffer.pop()
    options.buffer.push(popped)
    
    options.colors.remove(start)
    options.colors.insert(left_middle, popped)
    
    options.colors.remove(end)
    options.colors.insert(right_middle, popped)
    render(options)


