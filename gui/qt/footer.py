from gui.qt.common import *


def transform_icon(icon, fx, fy):
    transform = QTransform()
    transform.scale(fx, fy)
    transformed_icon = icon.transformed(transform)
    return transformed_icon


class QPushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.__active = None
        
    def get_active(self):
        return self.__active
    
    def set_active(self, b):
        if b == None:
            b = False
        elif b == self.__active:
            return
        self.__active = b 
        self.setEnabled(b)
        if b:
            self.setStyleSheet(f'background-color: rgb(0,196,240);')
        else:
            self.setStyleSheet(f'background-color: rgb(135,135,135);')
            
    active = property(get_active, set_active)


class FOOTER(QLabel):
    def __init__(self, *args, **kwargs):
        active = kwargs.pop('active', 0)
        super().__init__(*args, **kwargs)

        self.setGeometry(QRect(0, SCREEN_HEIGHT-80, SCREEN_WIDTH, 80)) 
        self.setFixedSize(SCREEN_WIDTH, 80)
        self.setObjectName('footer_bg')
        
        self.btns = {
            'left'  : QPushButton(self, objectName='footer_btn_txt', text=''), # ← ⟵ ⬅ ⏴⇦ ⇽ 🠐U+1F810
            'right' : QPushButton(self, objectName='footer_btn_txt', text=''), # → 🠒U+1F812
            ' '     : QPushButton(self, objectName='footer_btn_txt', text=''),
            'ok'    : QPushButton(self, objectName='footer_btn_txt', text='OK'),
        }

        right_icon = QPixmap(vp.images + 'right_arrow.png')        
        self.btns['right'].setIcon(QIcon(right_icon))
        self.btns['right'].setIconSize(right_icon.scaledToHeight(30).size())

        left_icon = transform_icon(right_icon, -1, 1)
        self.btns['left'].setIcon(QIcon(left_icon))
        self.btns['left'].setIconSize(left_icon.scaledToHeight(30).size())

        for i, (k, v) in enumerate(self.btns.items()): 
            v.setGeometry(QRect(i*137+(i+1)*50, 0, 137, 60))

        self.set_active(active)
        
    def set_active(self, b: int):
        b &= 0b1111
        for i, (k, v) in enumerate(self.btns.items()):
            v.active = b >> (3 - i) & 0b1




if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    qapp = QApplication(sys.argv)
    with open(vp.assets + 'style.css', 'r') as f:
        qapp.setStyleSheet(f.read())
    gui = QLabel()
    background = QLabel(gui)
    background.setGeometry(QRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    background.setScaledContents(True)
    page = FOOTER(gui)

    if os.name == 'nt':
        page.setGeometry(QRect(0, 0,int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        gui.resize(int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
        gui.show()
    else: gui.showFullScreen()
    
    
    page.show()
    input("")