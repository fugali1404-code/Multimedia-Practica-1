# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'practica1.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(838, 577)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(540, 70, 271, 141))
        font = QFont()
        font.setFamilies([u"Rage"])
        font.setPointSize(24)
        font.setItalic(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"background-color: rgb(85, 0, 0);\n"
"color: white;")
        self.imagenPedro = QLabel(Dialog)
        self.imagenPedro.setObjectName(u"imagenPedro")
        self.imagenPedro.setGeometry(QRect(280, 30, 220, 220))
        self.imagenPedro.setStyleSheet(u"background-image: url(\"C:/Users/User/Downloads/pedropedro.png\");\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 110px;\n"
"border: none;")
        self.botonIzq = QPushButton(Dialog)
        self.botonIzq.setObjectName(u"botonIzq")
        self.botonIzq.setGeometry(QRect(30, 310, 241, 41))
        font1 = QFont()
        font1.setFamilies([u"Rage"])
        font1.setPointSize(18)
        font1.setItalic(True)
        self.botonIzq.setFont(font1)
        self.botonDer = QPushButton(Dialog)
        self.botonDer.setObjectName(u"botonDer")
        self.botonDer.setGeometry(QRect(30, 370, 241, 41))
        self.botonVert = QPushButton(Dialog)
        self.botonVert.setObjectName(u"botonVert")
        self.botonVert.setGeometry(QRect(30, 430, 241, 41))
        self.botonHor = QPushButton(Dialog)
        self.botonHor.setObjectName(u"botonHor")
        self.botonHor.setGeometry(QRect(30, 480, 241, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rage'; font-size:24pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Multimedia <br />Practica 1</span></p></body></html>", None))
        self.imagenPedro.setText("")
        self.botonIzq.setText(QCoreApplication.translate("Dialog", u"girar 90\u00b0 izquierda", None))
        self.botonDer.setText(QCoreApplication.translate("Dialog", u"girar 90\u00b0 derecha", None))
        self.botonVert.setText(QCoreApplication.translate("Dialog", u"Espejo vertical", None))
        self.botonHor.setText(QCoreApplication.translate("Dialog", u"Espejo horizontal ", None))
    # retranslateUi

