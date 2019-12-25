# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce_gerenjingli.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import zhuce
import zhuce_jiaoyujingli
import zhuce_gongzuojingli
class Ui_gerenjingli(object):

    def gongzuojingli(self):
        self.form.close()
        Form4 = QtWidgets.QMainWindow()
        self.ui = zhuce_gongzuojingli.Ui_Form()
        self.ui.setupUi(Form4)
        Form4.show()
    def jiaoyujingli(self):
        self.form.close()
        Form2 = QtWidgets.QMainWindow()
        self.ui = zhuce_jiaoyujingli.Ui_Form()
        self.ui.setupUi(Form2)
        Form2.show()

    def gerenjingli(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = zhuce_gongzuojingli.Ui_Form()
        self.ui.setupUi(Form1)
        Form1.show()


    def wancheng(self):
        self.form.close()
        Form3 = QtWidgets.QMainWindow()
        self.ui = zhuce.Ui_zhuce()
        self.ui.setupUi(Form3)
        Form3.show()
    def setupUi(self, gerenjingli):
        gerenjingli.setObjectName("gerenjingli")
        gerenjingli.resize(459, 169)
        gerenjingli.setStyleSheet("background-image: url(:/res/white.jpg);")
        self.form = gerenjingli
        self.pushButton = QtWidgets.QPushButton(gerenjingli)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 93, 28))
        self.pushButton.setStyleSheet("font: 10pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(gerenjingli)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 40, 93, 28))
        self.pushButton_2.setStyleSheet("font: 10pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(gerenjingli)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 110, 93, 28))
        self.pushButton_3.setStyleSheet("font: 10pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(gerenjingli)
        self.pushButton.clicked.connect(self.gongzuojingli)
        self.pushButton_2.clicked.connect(self.jiaoyujingli)
        self.pushButton_3.clicked.connect(self.wancheng)
        QtCore.QMetaObject.connectSlotsByName(gerenjingli)

    def retranslateUi(self, gerenjingli):
        _translate = QtCore.QCoreApplication.translate
        gerenjingli.setWindowTitle(_translate("gerenjingli", "Form"))
        self.pushButton.setText(_translate("gerenjingli", "工作经历"))
        self.pushButton_2.setText(_translate("gerenjingli", "教育经历"))
        self.pushButton_3.setText(_translate("gerenjingli", "完成"))

import picture_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_gerenjingli()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())