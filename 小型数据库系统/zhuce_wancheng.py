# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce_wancheng.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wancheng(object):
    def setupUi(self, wancheng):
        wancheng.setObjectName("wancheng")
        wancheng.resize(315, 110)
        wancheng.setStyleSheet("background-image: url(:/res/white.jpg);")
        self.form = wancheng
        self.pushButton = QtWidgets.QPushButton(wancheng)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton.setObjectName("pushButton")
        self.info = QtWidgets.QLabel(wancheng)
        self.info.setGeometry(QtCore.QRect(70, 10, 191, 41))
        self.info.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 9pt \"幼圆\";")
        self.info.setText("")
        self.info.setObjectName("info")

        self.retranslateUi(wancheng)
        self.pushButton.clicked.connect(wancheng.close)
        QtCore.QMetaObject.connectSlotsByName(wancheng)

    def retranslateUi(self, wancheng):
        _translate = QtCore.QCoreApplication.translate
        wancheng.setWindowTitle(_translate("wancheng", "Form"))
        self.pushButton.setText(_translate("wancheng", "确定"))

import picture_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_wancheng()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())