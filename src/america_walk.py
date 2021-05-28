from utils import walk, translate, render

RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

def translate(start,end,stepSize):
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
    while (c1 != c2):
        c1= (translate(c1[0],c2[0],options.step),translate(c1[1],c2[1],options.step),translate(c1[2],c2[2],options.step))
        options.buffer.push(c1)

def america_walk(options):
    if len(options.buffer) == 0:
        walk(RED, WHITE, options)
        walk(WHITE, BLUE, options)
        walk(BLUE, WHITE, options)
        walk(WHITE, RED, options)
        
    popped = options.buffer.pop()
    options.colors.push(popped)
    options.buffer.push(popped)
    render(options)


