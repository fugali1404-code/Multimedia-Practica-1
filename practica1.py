
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtWidgets
from practica1_ui import Ui_Dialog
import cv2 as cv
import sys


class Ventana(QDialog, Ui_Dialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Cargar imagen
        self.img = cv.imread("pedropedro.png")

        if self.img is None:
            raise FileNotFoundError("No se encontró la imagen")

        self.imagenPedro.setStyleSheet("background-color: transparent;")
        self.imagenPedro.setScaledContents(True)
        self.mostrar_imagen()

        # Conectar botones
        self.botonDer.clicked.connect(self.girar_derecha)
        self.botonIzq.clicked.connect(self.girar_izquierda)
        self.botonVert.clicked.connect(self.espejo_vertical)
        self.botonHor.clicked.connect(self.espejo_horizontal)

    # Mostrar imagen
    def mostrar_imagen(self):
        self.imagenPedro.setPixmap(self.convert_cv_qt(self.img))

    # Girar 90 grados a la derecha
    def girar_derecha(self):
        self.img = cv.rotate(self.img, cv.ROTATE_90_CLOCKWISE)
        self.mostrar_imagen()

    # Girar 90 grados a la izquierda
    def girar_izquierda(self):
        self.img = cv.rotate(self.img, cv.ROTATE_90_COUNTERCLOCKWISE)
        self.mostrar_imagen()

    # Espejo vertical
    def espejo_vertical(self):
        self.img = cv.flip(self.img, 0)
        self.mostrar_imagen()

    # Espejo horizontal
    def espejo_horizontal(self):
        self.img = cv.flip(self.img, 1)
        self.mostrar_imagen()

    # Convertir imagen de OpenCV a Qt
    def convert_cv_qt(self, cv_img):
        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        converted_image = QImage(
            rgb_image.data,
            w,
            h,
            bytes_per_line,
            QImage.Format.Format_RGB888
        )

        return QPixmap.fromImage(converted_image)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())
