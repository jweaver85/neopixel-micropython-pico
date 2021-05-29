import neopixel
from machine import Pin

from options import Options
from queue import queue
from rainbowwalk import rainbowwalk
from split_rainbow_walk import split_rainbow_walk
from edie_walk import edie_walk
from split_edie_walk import split_edie_walk
from america_walk import america_walk
from split_america_walk import split_america_walk
from color_walk import color_walk
from split_color_walk import split_color_walk
from sparkle import sparkle
from sparkle_shift import sparkle_shift
from black_light import black_light

# Update this to match the number of NeoPixel LEDs connected to your board.
# TODO: buy another strip and see if the board can drive more than on strip (shared colors and buffers!)
num_pixels = 60
options = Options(
    num_pixels,  # pixels in this LED strip
    2,  # step size for walks
    0.1,  # brightness
    0.01,  # sleepytime (unused?)
    neopixel.NeoPixel(0, num_pixels),  # neopixel object
    queue([], num_pixels),  # colors to be rendered (buffer 1)
    queue([], None),  # buffer (buffer 2) to consumed by buffer 1
    'rainbowwalk',  # initial color effect to start TODO: move this to onboard storage
    False  # debug mode (for logging purposes
)

algos = [sparkle, black_light, rainbowwalk, edie_walk, america_walk, color_walk]
algo_index = 0

options.pixels.brightness = options.brightness
options.pixels.auto_write = False

algo_button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
algo_button_prev = False

brightness_button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
brightness_button_prev = False

def updateAlgorithm():
    global algo_button
    global algo_button_prev
    global algo_index
    global algos

    if algo_button.value() and algo_button.value() != algo_button_prev:
        algo_button_prev = algo_button.value()
        new_algo_index = (algo_index + 1) % (len(algos) + 1)

        if algo_index != new_algo_index:
            options.buffer.clear()

        algo_index = new_algo_index
        options.algo = algos[algo_index] if algo_index < len(algos) else "off"

        if options.debug: print("algo_button pressed! Current algo: " + str(options.algo))

    if not algo_button.value():
        algo_button_prev = algo_button.value()

    return options.algo


def updateBrightness():
    global options
    global brightness_button
    global brightness_button_prev

    if brightness_button.value() and brightness_button.value() != brightness_button_prev:
        brightness_button_prev = brightness_button.value()

        options.brightness = float(options.brightness + 0.1) if float(options.brightness + 0.1) < 1.01 else 0
        return options.brightness

        if options.debug: print("brightness_button pressed! Current brightness: " + str(options.brightness))

    if not brightness_button.value():
        brightness_button_prev = brightness_button.value()

    return options.brightness


def updateStep():
    #     global step_pot
    #     global options
    #     calculated = int((step_pot.value / 65530) * 255)
    #     calculated = calculated if calculated > 0 else 1
    #     difference = abs(options.step - calculated)
    #     print(str(calculated))
    #     if difference >= 2:
    #         options.buffer.clear()s
    #         return calculated if calculated > 0 else 1
    #     else:
    return options.step


def do_work(options):  # setup == "do_work"
    global algos
    global algo_index

    options.algo = updateAlgorithm()
    options.brightness = updateBrightness()
    options.step = updateStep()

    if algo_index == len(algos):
        options.pixels.fill((0, 0, 0))
        options.pixels.write()
    else:
        options.pixels.brightness = options.brightness
        algos[algo_index](options)

    if options.debug: print("numpixels" + str(options.num_pixels))


while True:
    do_work(options)
