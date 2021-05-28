from utils import translate, walk, render

COLOR01 = (255, 0, 0)
COLOR02 = (255, 85, 0)
COLOR03 = (255, 230, 0)
COLOR04 = (0, 255, 0)
COLOR05 = (0, 255, 68)
COLOR06 = (0, 255, 208)
COLOR07 = (0, 110, 255)
COLOR08 = (0, 0, 255)
COLOR09 = (157, 0, 255)
COLOR10 = (255, 0, 200)

def split_rainbow_walk(options):
    if len(options.buffer) == 0:
        walk(COLOR01, COLOR02, options)
        walk(COLOR02, COLOR03, options)
        walk(COLOR03, COLOR04, options)
        walk(COLOR04, COLOR05, options)
        walk(COLOR05, COLOR06, options)
        walk(COLOR06, COLOR07, options)
        walk(COLOR07, COLOR08, options)
        walk(COLOR08, COLOR09, options)
        walk(COLOR09, COLOR10, options)
        walk(COLOR10, COLOR01, options)
     
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

