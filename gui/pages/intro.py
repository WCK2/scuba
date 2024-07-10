from gui.qt.common import *


class INTRO(NFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('page_intro')

        bg = QLabel(self)
        bg.setStyleSheet('background-color: rgb(255,255,255)')
        bg.setGeometry(QRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        logo = QLabel(self, alignment=Qt.AlignCenter)
        pixmap = QPixmap(vp.images + 'Logo EyPISA')
        logo.setPixmap(pixmap)
        logo.setFixedSize(pixmap.size())

        self.footer = FOOTER(self, active=0b0101)
        self.footer.btns['ok'].clicked.connect(gsig.next_page.emit)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(settings.header_height)
        layout.addWidget(logo, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.footer)

        gsig.soft_key_pressed.connect(self.__handle_soft_key_press)


    def __handle_soft_key_press(self, key_id):
        if key_id == 'sk4': gsig.next_page.emit()
        else: pass

    #~ PyQt Events
    def showEvent(self, a0):
        gsig.set_soft_keys.emit(0b0101)
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
    page = INTRO(gui)
    if os.name == 'nt':
        page.setGeometry(QRect(0, 0,int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        gui.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        gui.show()
    else: gui.showFullScreen()
    
    page.show()
    input("")
