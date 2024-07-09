from gui.qt.nframe import *
from gui.qt.nstackedwidget import NStackedWidget
from utils.config import vp, settings
from gui.workers.ntimer import NTimer
from gui.qt.footer import FOOTER


signal.signal(signal.SIGINT, signal.SIG_DFL)    
qapp = QApplication(sys.argv)

class GlobalSignals(QObject):
    previous_page = pyqtSignal()
    next_page = pyqtSignal()
    goto_page = pyqtSignal(str)

    enable_soft_key = pyqtSignal(str)
    disable_soft_key = pyqtSignal(str)
    set_soft_keys = pyqtSignal(int)
    soft_key_pressed = pyqtSignal(str)

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(GlobalSignals, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

gsig = GlobalSignals()


class FOOTER(FOOTER):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btns['left'].clicked.connect(gsig.previous_page.emit)
        self.btns['right'].clicked.connect(gsig.next_page.emit)





