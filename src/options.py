class Options:
    #static CLASS variable
    static_variable = 'static variable'
                   
    def __init__(self, num_pixels, step, brightness, sleepytime, pixels, colors, buffer, algo, debug):
        # instance variables
        self.num_pixels = num_pixels
        self.step = step
        self.brightness = brightness
        self.sleepytime = sleepytime
        self.pixels = pixels
        self.colors = colors
        self.buffer = buffer
        self.algo = algo
        self.debug = debug
