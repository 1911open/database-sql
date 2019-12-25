# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sorry.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Main
class Ui_sorry(object):

    def zhuye(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Main.Ui_Welcome()
        self.ui.setupUi(Form1)
        Form1.show()



    def setupUi(self, sorry):
        sorry.setObjectName("sorry")
        sorry.setWindowModality(QtCore.Qt.NonModal)
        sorry.resize(373, 173)
        sorry.setStyleSheet("border-image: url(:/res/white.jpg);")
        self.form = sorry
        self.label = QtWidgets.QLabel(sorry)
        self.label.setGeometry(QtCore.QRect(100, 30, 171, 41))
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(sorry)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 91, 41))
        self.pushButton.setStyleSheet("border-image: url(:/res/denglu.jpg);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(sorry)
        self.pushButton.clicked.connect(self.zhuye)
        QtCore.QMetaObject.connectSlotsByName(sorry)

    def retranslateUi(self, sorry):
        _translate = QtCore.QCoreApplication.translate
        sorry.setWindowTitle(_translate("sorry", "Sorry"))
        self.label.setText(_translate("sorry", "敬请期待！"))

import picture_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_sorry()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
