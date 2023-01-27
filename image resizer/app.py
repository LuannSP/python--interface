import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class New(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnArchive.clicked.connect(self.load_image)
        self.btnRed.clicked.connect(self.resize_image)
        self.btnSave.clicked.connect(self.save_image)

    def load_image(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Selecionar Imagem',
            r'C:\Users\luann\Pictures'
        )
        self.inputArchive.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.lblImage.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeigth.setText(str(self.original_img.height()))

    def resize_image(self):
        width = int(self.inputWidth.text())
        self.new_image = self.original_img.scaledToWidth(width)
        self.lblImage.setPixmap(self.new_image)
        self.inputWidth.setText(str(self.new_image.width()))
        self.inputHeigth.setText(str(self.new_image.height()))
    
    def save_image(self):
        locate, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            'C:\\Users\\luann\\Desktop\\'
        )
        self.new_image.save(locate, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = New()
    new.show()
    qt.exec_()
