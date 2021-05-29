import uarray
import rp2
from machine import Pin
from queue import queue


class NeoPixel:

    @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
    def ws2812():
        T1 = 2
        T2 = 5
        T3 = 3
        wrap_target()
        label("bitloop")
        out(x, 1).side(0)[T3 - 1]
        jmp(not_x, "do_zero").side(1)[T1 - 1]
        jmp("bitloop").side(1)[T2 - 1]
        label("do_zero")
        nop().side(0)[T2 - 1]
        wrap()

    def __init__(self, pin, num_pixels):
        self.brightness = 0.01
        # Create the StateMachine with the ws2812 program, outputting on Pin(16).
        self.__sm = rp2.StateMachine(0, self.ws2812, freq=8_000_000, sideset_base=Pin(pin))
        # Start the StateMachine, it will wait for data on its FIFO.
        self.__sm.active(1)
        # Display a pattern on the LEDs via an array of LED RGB values.

        self.__num_pixels = num_pixels
        # self.pixels = [0] * num_pixels # list([0] * num_pixels)# uarray.array("I", range(num_pixels))
        self.pixels = [0] * num_pixels

    def write(self):
        dimmer_ar = uarray.array("I", [0 for _ in range(self.__num_pixels)])
        for i, c in enumerate(self.pixels):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g << 16) + (r << 8) + b
        self.__sm.put(dimmer_ar, 8)

    def update(self, i, color):
        self.pixels[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    def fill(self, color):
        for i in range(len(self.pixels)):
            self.update(i, color)

