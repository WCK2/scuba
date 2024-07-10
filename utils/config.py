import os


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480


class VPath:
    def __init__(self) -> None:
        self.assets = os.getcwd() + '/assets/'
        self.images = os.getcwd() + '/assets/images/'

vp = VPath()


class SETTINGS:
    def __new__(cls, *args, **kw):
         if not hasattr(cls, '_instance'):
             orig = super(SETTINGS, cls)
             cls._instance = orig.__new__(cls, *args, **kw)
         return cls._instance
    def __init__(self): 
        #? gui
        self.volume = 5
        self.header_height = 0
        self.footer_height = 125

        #? io
        self.soft_keys = {
            'sk1': {'input_pin': 26, 'led_pin': 22, 'enabled': False},
            'sk2': {'input_pin': 16, 'led_pin': 23, 'enabled': False},
            'sk3': {'input_pin': 6, 'led_pin': 24, 'enabled': False},
            'sk4': {'input_pin': 5, 'led_pin': 25, 'enabled': False},
        }
        self.buzzer_pin = 4

    def reset(self):
        pass

settings = SETTINGS()



