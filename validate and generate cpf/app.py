import design
import sys
from cpf import validateCpf, generateCpf
from PyQt5.QtWidgets import QApplication, QMainWindow

class Form(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnVal.clicked.connect(self.valid_cpf)
        self.btnGen.clicked.connect(self.gen_cpf)

    def valid_cpf(self):
        cpf = self.inputCpf.text()
        self.lineReturn.setText(
            str(validateCpf(cpf))
        )

    def gen_cpf(self):
        self.lineReturn.setText(
            str(generateCpf())
        )

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = Form()
    new.show()
    qt.exec_()
