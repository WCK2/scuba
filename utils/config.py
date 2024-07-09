import os


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480


class VPath:
    def __init__(self) -> None:
        self.assets = os.getcwd() + '/assets/'
        self.images = os.getcwd() + '/assets/images/'

vp=VPath()


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
            'sk1': {'input_pin': 17, 'led_pin': 27, 'enabled': False},
            'sk2': {'input_pin': 22, 'led_pin': 10, 'enabled': False},
            'sk3': {'input_pin': 9, 'led_pin': 11, 'enabled': False},
            'sk4': {'input_pin': 0, 'led_pin': 5, 'enabled': False},
        }

    def reset(self):
        pass

settings = SETTINGS()



