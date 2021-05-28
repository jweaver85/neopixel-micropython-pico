import neopixel
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

algos = [sparkle, black_light, rainbowwalk, split_rainbow_walk, edie_walk, split_edie_walk, america_walk,
         split_america_walk,
         color_walk, split_color_walk, sparkle, sparkle_shift]
algo_index = 0

options.pixels.brightness = options.brightness
options.pixels.auto_write = False


# algo_button = digitalio.DigitalInOut(board.GP13)
# algo_button.switch_to_input(pull=digitalio.Pull.DOWN)
# algo_button_prev = False

# brightness_button = digitalio.DigitalInOut(board.GP12)
# brightness_button.switch_to_input(pull=digitalio.Pull.DOWN)
# brightness_button_prev = False

# step_pot = analogio.AnalogIn(board.GP26)
# brightness_pot = analogio.AnalogIn(board.GP27)


def updateAlgorithm():
    #     global algo_button
    #     global algo_button_prev
    #     global algo_index
    #     global algos
    #
    #     if algo_button.value and algo_button.value != algo_button_prev:
    #         algo_button_prev = algo_button.value
    #         new_algo_index = (algo_index + 1) % (len(algos) + 1)
    #
    #         if algo_index != new_algo_index:
    #             options.buffer.clear()
    #
    #         algo_index = new_algo_index
    #         options.algo = algos[algo_index] if algo_index < len(algos) else "off"
    #
    #         if options.debug: print("algo_button pressed! Current algo: " + str(options.algo))
    #
    #     if not algo_button.value:
    #         algo_button_prev = algo_button.value
    #
    return options.algo


def updateBrightness():
    #     global brightness_pot
    #     global options
    #
    #     calculated = float(brightness_pot.value / 65530)  # - 0.01
    #     options.brightness = calculated if abs(calculated - options.brightness) > 0.05 else options.brightness
    return options.brightness


def updateStep():
    #     global step_pot
    #     global options
    #     calculated = int((step_pot.value / 65530) * 255)
    #     calculated = calculated if calculated > 0 else 1
    #     difference = abs(options.step - calculated)
    #     print(str(calculated))
    #     if difference >= 2:
    #         options.buffer.clear()
    #         return calculated if calculated > 0 else 1
    #     else:
    return options.step


def do_work():  # setup == "do_work"
    global algos
    global algo_index
    global options

    options.algo = updateAlgorithm()
    options.brightness = updateBrightness()
    options.step = updateStep()

    if algo_index == len(algos):
        options.pixels.fill((0, 0, 0))
        options.pixels.write()
    else:
        options.pixels.brightness = options.brightness
        algos[algo_index](options)

    if (options.debug): print("numpixels" + str(options.num_pixels))


while True:
    do_work()

