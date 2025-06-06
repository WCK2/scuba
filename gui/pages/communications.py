from gui.qt.common import *


class COMMUNICATIONS(NFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("page_communications")

        bg = QLabel(self)
        pixmap = QPixmap(vp.images + 'bg2')
        bg.setPixmap(pixmap)
        bg.setFixedSize(pixmap.size())

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(settings.header_height)
        layout.addWidget(QLabel(self, objectName='G1', text='COMMUNICATIONS'))
        layout.addStretch()

        self.footer = FOOTER(self, active=0b1100)

        layout.addStretch()
        layout.addWidget(self.footer)


    #~ PyQt Events
    def showEvent(self, a0):
        gsig.set_soft_keys.emit(0b1100)
        return super().enterEvent(a0)

    def enterEvent(self, a0):
        return super().enterEvent(a0)

    def hideEvent(self, a0) -> None:
        return super().hideEvent(a0)




if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    with open(vp.assets + 'style.css', 'r') as f:
        app.setStyleSheet(f.read())

    gui = QLabel()
    page = COMMUNICATIONS(gui)
    if os.name == 'nt':
        page.setGeometry(QRect(0, 0,int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        gui.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        gui.show()
    else: gui.showFullScreen()
    
    page.show()
    input("")
