# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 500)
        Dialog.setMinimumSize(QtCore.QSize(800, 500))
        Dialog.setMaximumSize(QtCore.QSize(800, 500))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb")
        font.setPointSize(15)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(120, 108, 255);\n"
"}")
        Dialog.setModal(False)
        self.btn_persion = QtWidgets.QPushButton(Dialog)
        self.btn_persion.setGeometry(QtCore.QRect(400, 390, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.btn_persion.setFont(font)
        self.btn_persion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_persion.setStyleSheet("color: white;\n"
"background-color: rgb(34, 34, 34);\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-top: none;\n"
"border-bottom-right-radius: 15;\n"
"border-left: none;\n"
"")
        self.btn_persion.setObjectName("btn_persion")
        self.btn_english = QtWidgets.QPushButton(Dialog)
        self.btn_english.setGeometry(QtCore.QRect(50, 390, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.btn_english.setFont(font)
        self.btn_english.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_english.setStyleSheet("color: white;\n"
"background-color: rgb(34, 34, 34);\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-top: none;\n"
"border-bottom-left-radius: 15;")
        self.btn_english.setObjectName("btn_english")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 700, 350))
        font = QtGui.QFont()
        font.setFamily("IRANSansWeb")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: white;\n"
"font: 14pt \"IRANSansWeb\";\n"
"background-color: #222;\n"
"border: 1px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"padding: 20px;")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        self.btn_persion.clicked.connect(self.textEdit.clear) # type: ignore
        self.btn_english.clicked.connect(self.textEdit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_persion.setText(_translate("Dialog", "Persion"))
        self.btn_english.setText(_translate("Dialog", "English"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())