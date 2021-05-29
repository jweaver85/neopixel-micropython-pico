import machine
import time
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

index = 0


def callback():
    global index
    index = index + 1
    print("index: " + index)


button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)


while True:
    # first = button.value()
    # time.sleep(0.01)
    # second = button.value()
    # if first and not second:
    #     print('Button pressed!')
    # elif not first and second:
    #     print('Button released!')
