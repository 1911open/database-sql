# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import picture_rc
import zhuce
import sorry
class Ui_Welcome(object):

    def ttz(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = zhuce.Ui_zhuce()
        self.ui.setupUi(Form1)
        Form1.show()

    def ttd(self):
        self.form.close()
        Form2 = QtWidgets.QMainWindow()
        self.ui = sorry.Ui_sorry()
        self.ui.setupUi(Form2)
        Form2.show()


    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.setWindowModality(QtCore.Qt.ApplicationModal)
        Welcome.resize(380, 480)
        Welcome.setStyleSheet("background-image: url(:/res/white.jpg);")
        self.form = Welcome
        self.logo = QtWidgets.QLabel(Welcome)
        self.logo.setGeometry(QtCore.QRect(95, 50, 190, 161))
        self.logo.setStyleSheet("border-image: url(:/res/girl.jpg);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(Welcome)
        self.label.setGeometry(QtCore.QRect(0, 324, 401, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Welcome)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 290, 191, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.zhuce = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.zhuce.setStyleSheet("border-image: transparent;\n"
"background-image: transparent;\n"
"font: 20pt \"幼圆\";\n"
"color: rgb(0, 0, 255);\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/denglu.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zhuce.setIcon(icon)
        self.zhuce.setIconSize(QtCore.QSize(30, 20))
        self.zhuce.setCheckable(False)
        self.zhuce.setAutoRepeat(False)
        self.zhuce.setObjectName("zhuce")
        self.verticalLayout.addWidget(self.zhuce)
        self.denglu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.denglu.setStyleSheet("border-image: transparent;\n"
"background-image: transparent;\n"
"font: 20pt \"幼圆\";\n"
"color: rgb(0, 0, 255);\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/zhuce.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.denglu.setIcon(icon1)
        self.denglu.setIconSize(QtCore.QSize(20, 20))
        self.denglu.setCheckable(False)
        self.denglu.setAutoRepeat(False)
        self.denglu.setObjectName("denglu")
        self.verticalLayout.addWidget(self.denglu)

        self.retranslateUi(Welcome)
        self.zhuce.clicked.connect(self.ttz)
        self.denglu.clicked.connect(self.ttd)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Welcome"))
        self.zhuce.setText(_translate("Welcome", "  注册"))
        self.denglu.setText(_translate("Welcome", "   登陆"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Welcome()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())