from gui.qt.common import *
from gui.workers.gpio_thread import GPIOThread
from gui.pages.intro import INTRO
from gui.pages.home import HOME
from gui.pages.communications import COMMUNICATIONS
from gui.pages.air_compressor import AIR_COMPRESSOR
from gui.pages.battery import BATTERY
from gui.pages.alarms import ALARMS
from gui.pages.maintenance import MAINTENANCE
from gui.pages.setup import SETUP
import os
if os.name == 'nt': import utils.mock_gpio as GPIO
else: import RPi.GPIO as GPIO
import atexit


class SCUBA_GUI(NStackedWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #~ header
        # header_container = QFrame(self, objectName='banner')
        # header_container.setGeometry(QRect(0, 0, SCREEN_WIDTH, settings.header_height))
        # header_panel = QHBoxLayout(header_container)
        # header_panel.setContentsMargins(0, 0, 0, 0)
        # self.header_title=QLabel(self, objectName='G1', text='main', minimumWidth=800)

        # header_panel.addSpacing(20)
        # header_panel.addStretch()
        # header_panel.addWidget(self.header_title)
        # header_panel.addStretch()
        # header_panel.addSpacing(20)

        #~ pages
        self.page_intro             : INTRO = self.addWidget(INTRO())
        self.page_home              : HOME = self.addWidget(HOME())
        self.page_communications    : COMMUNICATIONS = self.addWidget(COMMUNICATIONS())
        self.page_air_compressor    : AIR_COMPRESSOR = self.addWidget(AIR_COMPRESSOR())
        self.page_battery           : BATTERY = self.addWidget(BATTERY())
        self.page_alarms            : ALARMS = self.addWidget(ALARMS())
        self.page_maintenance       : MAINTENANCE = self.addWidget(MAINTENANCE())
        self.page_setup             : SETUP = self.addWidget(SETUP())

        #~ signals
        gsig.previous_page.connect(self.__previous_page)
        gsig.next_page.connect(self.__next_page)
        gsig.goto_page.connect(lambda s: self.__gotopage(s))
        gsig.soft_key_pressed.connect(self.__handle_soft_key_press)

        gsig.haptic_feedback.connect(self.__haptic_feedback)

        #~ timers
        self.haptic_feedback_timer = NTimer(500, lambda: self.__haptic_feedback(0), False)


    def __handle_soft_key_press(self, key_id):
        if key_id == 'sk1': self.__previous_page()
        elif key_id == 'sk2': self.__next_page()
        else: pass

    def __gotopage(self,name:str):
        if name == 'intro':
            self.setCurrentWidget(self.page_intro)
        elif name == 'home':
            self.setCurrentWidget(self.page_home)
        elif name == 'communications':
            self.setCurrentWidget(self.page_communications)
        elif name == 'air_compressor':
            self.setCurrentWidget(self.page_air_compressor)
        elif name == 'battery':
            self.setCurrentWidget(self.page_battery)
        elif name == 'alarms':
            self.setCurrentWidget(self.page_alarms)
        elif name == 'maintenance':
            self.setCurrentWidget(self.page_maintenance)
        elif name == 'setup':
            self.setCurrentWidget(self.page_setup)

    def __previous_page(self):
        self.setCurrentIndex(self.currentIndex()-1)

    def __next_page(self):
        self.setCurrentIndex(self.currentIndex()+1)

    def reset(self):
        self.setCurrentWidget(self.page_home)

    def __haptic_feedback(self, b):
        if b:
            if self.haptic_feedback_timer.isRunning():
                self.haptic_feedback_timer.reset()
            else:
                self.haptic_feedback_timer.start()
            GPIO.output(settings.buzzer_pin, GPIO.HIGH)
        else:
            if self.haptic_feedback_timer.isRunning:
                self.haptic_feedback_timer.stop()
            GPIO.output(settings.buzzer_pin, GPIO.LOW)

    def setCurrentIndex(self, index: int) -> None:
        return super().setCurrentIndex(index)
        
    def setCurrentWidget(self, w: QWidget) -> None:
        return super().setCurrentWidget(w)

    def hideEvent(self, a0: QHideEvent) -> None:
        return super().hideEvent(a0)
        
    def showEvent(self, a0: QShowEvent) -> None:
        return super().showEvent(a0)


if __name__ == "__main__":
    gpio_thread = GPIOThread()
    gpio_thread.start()
    atexit.register(lambda: gpio_thread.stop())

    with open(vp.assets + 'style.css', 'r') as f:
        qapp.setStyleSheet(f.read())
    
    app = SCUBA_GUI()
    app.setFixedSize(QSize(800,480))
    atexit.register(lambda: app.__haptic_feedback(0))

    if os.name == 'nt':
        app.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        app.show()
    else:
        app.showFullScreen()

    input("")

