import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import uic

class principal(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        uic.loadUi('PrimerEjercicio.ui',self)
        self.show()

def main():
    app = PyQT.QApplication([])
    window = principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()