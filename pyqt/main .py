import PyQt6.QtWidgets as qtw

class window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.show()

app = qtw.QApplication([])
mw = window()

app.exec()
