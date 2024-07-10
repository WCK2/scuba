import time


BCM = 'BCM'
IN = 'IN'
OUT = 'OUT'
PUD_DOWN = 'PUD_DOWN'
PUD_UP = 'PUD_UP'
LOW = False
HIGH = True


class MockGPIO:
    def __init__(self):
        self.pins = {}

    def setmode(self, mode):
        print(f'GPIO mode set to {mode}')

    def setup(self, pin, mode, pull_up_down=None):
        self.pins[pin] = {'mode': mode, 'state': LOW}
        # print(f'Pin {pin} set to mode {mode} with pull {pull_up_down}')

    def input(self, pin):
        return self.pins[pin]['state']

    def output(self, pin, state):
        self.pins[pin]['state'] = state
        # print(f'Pin {pin} set to {state}')

    def cleanup(self):
        print('GPIO cleanup')
        self.pins.clear()


GPIO = MockGPIO()
time = time

setmode = GPIO.setmode
setup = GPIO.setup
input = GPIO.input
output = GPIO.output
cleanup = GPIO.cleanup


