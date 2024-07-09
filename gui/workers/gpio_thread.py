from PyQt5.QtCore import QThread
from gui.qt.common import gsig
from utils.config import settings
import time
import os

if os.name == 'nt':
    import utils.mock_gpio as GPIO
else:
    import RPi.GPIO as GPIO


class GPIOThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._running = True
        gsig.enable_soft_key.connect(self.enable_soft_key)
        gsig.disable_soft_key.connect(self.disable_soft_key)
        gsig.set_soft_keys.connect(self.set_soft_keys)

    def run(self):
        GPIO.setmode(GPIO.BCM)
        
        # Setup input and output pins
        for key in settings.soft_keys.values():
            GPIO.setup(key['input_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(key['led_pin'], GPIO.OUT)
        
        while self._running:
            for key_id, key in settings.soft_keys.items():
                if GPIO.input(key['input_pin']) == GPIO.HIGH and key['enabled']:
                    print(f'gsig.soft_key_pressed.emit({key_id})')
                    gsig.soft_key_pressed.emit(key_id)
                    # time.sleep(0.3)
                    QThread.msleep(300)

            # time.sleep(0.1)
            QThread.msleep(100)

    def stop(self):
        self._running = False
        GPIO.cleanup()
        self.wait()

    def enable_soft_key(self, key_id: str):
        settings.soft_keys[key_id]['enabled'] = True
        GPIO.output(settings.soft_keys[key_id]['led_pin'], GPIO.HIGH)

    def disable_soft_key(self, key_id: str):
        settings.soft_keys[key_id]['enabled'] = False
        GPIO.output(settings.soft_keys[key_id]['led_pin'], GPIO.LOW)

    def set_soft_keys(self, b: int):
        b &= 0b1111
        for i, (key_id, key) in enumerate(settings.soft_keys.items()):
            # key['enabled'] = b >> (3 - i) & 0b1
            if b >> (3 - i) & 0b1:
                print(f'enable soft key: {key_id}')
                self.enable_soft_key(key_id)
            else:
                print(f'disable soft key: {key_id}')
                self.disable_soft_key(key_id)



