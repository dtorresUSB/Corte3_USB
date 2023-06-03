import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        

    def initGUI(self):
        uic.loadUi('App_calculoV2.ui',self)
        self.show()
        
        self.pushButton.clicked.connect(lambda: self.calcular(int(self.num2txt.text()),int(self.num1txt.text())))
        #self.pushButton.clicked.connect(self.calcular)
        self.actionCerrar.triggered.connect(exit)

    def calcular(self,uno,dos):
        if self.Sumar.isChecked()==True:
            self.resultado.setText(str(uno+dos))
        elif self.Restar.isChecked()==True:
            self.resultado.setText(str(uno-dos))
        elif self.Multiplicar.isChecked()==True:
            self.resultado.setText(str(uno*dos))
        else:
            self.resultado.setText(str(round(uno/dos,2)))

def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

