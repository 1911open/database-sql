# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import Main
import zhuce_wancheng
import zhuce_gerenjingli
from datetime import datetime

def regisster(name,sex,birth,id,password):

    if name == "" or password == "" or sex == "" or id == "" or birth == "":
        return 1
    try:
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='201314xIn', db='sz160110115', charset='utf8')
        cursor = db.cursor()
        sql_information = "replace into information (name,sex,birth,id,password) values (%s,%s,%s,%s,%s)"
        sql_dairy = "replace into dairy(id) values(%s)"
        sql_ee = "replace into ee(id,name) values(%s,%s)"
        sql_email = "replace into email(id) values(%s)"
        sql_friend = "replace into friend(id) values(%s)"
        sql_group1 = "replace into group1(id) values(%s)"
        sql_system1 = "replace into system1(id) values(%s)"
        sql_we = "replace into we(id,name) values(%s,%s)"
        sql_user = "replace into new_table(id,time) values(%s,%s)"
        res = [id]
        res1 = [name,sex,birth,id,password]
        res2 = [id,name]
        cursor.execute(sql_information,res1)
        cursor.execute(sql_ee, res2)
        cursor.execute(sql_email, res)
        cursor.execute(sql_friend, res)
        cursor.execute(sql_group1, res)
        cursor.execute(sql_system1, res)
        cursor.execute(sql_user, [id,datetime.now()])
        cursor.execute(sql_we, res2)
        db.commit()
        cursor.close()
        db.close()
        return 0
    except:
        pass


class Ui_zhuce(object):

    def gerenjingli(self):
        self.form.close()
        Form3 = QtWidgets.QMainWindow()
        self.ui = zhuce_gerenjingli.Ui_gerenjingli()
        self.ui.setupUi(Form3)
        Form3.show()


    def wancheng(self):
        Form2 = QtWidgets.QMainWindow()
        self.ui = zhuce_wancheng.Ui_wancheng()
        self.ui.setupUi(Form2)
        Form2.show()
        name = self.name.toPlainText()
        sex = self.sex.toPlainText()
        birth = self.birth.toPlainText()
        id = self.id.toPlainText()
        password = self.password.toPlainText()
        if regisster(name,sex,birth,id,password) == 0:
            information = "注册/修改成功"
        elif regisster(name,sex,birth,id,password) == 1:
            information = "输入不能为空"
        self.ui.info.setText(information)


    def tuichu(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Main.Ui_Welcome()
        self.ui.setupUi(Form1)
        Form1.show()




    def setupUi(self, zhuce):
        zhuce.setObjectName("zhuce")
        zhuce.resize(381, 427)
        zhuce.setStyleSheet("background-image: url(:/res/white.jpg);")
        self.form = zhuce
        self.label = QtWidgets.QLabel(zhuce)
        self.label.setGeometry(QtCore.QRect(70, 40, 31, 31))
        self.label.setStyleSheet("background-image: transpartent;\n"
"font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);\n"
"border-image: transpartent;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(zhuce)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 31, 31))
        self.label_2.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(zhuce)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 31, 31))
        self.label_3.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(zhuce)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 31, 31))
        self.label_4.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(zhuce)
        self.label_5.setGeometry(QtCore.QRect(70, 280, 31, 31))
        self.label_5.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(zhuce)
        self.label_6.setGeometry(QtCore.QRect(0, 320, 381, 41))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(zhuce)
        self.pushButton.setGeometry(QtCore.QRect(80, 390, 93, 28))
        self.pushButton.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(zhuce)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 340, 181, 28))
        self.pushButton_2.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(zhuce)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 387, 91, 31))
        self.pushButton_3.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.name = QtWidgets.QTextEdit(zhuce)
        self.name.setGeometry(QtCore.QRect(110, 40, 181, 31))
        self.name.setObjectName("name")
        self.sex = QtWidgets.QTextEdit(zhuce)
        self.sex.setGeometry(QtCore.QRect(110, 100, 181, 31))
        self.sex.setObjectName("sex")
        self.birth = QtWidgets.QTextEdit(zhuce)
        self.birth.setGeometry(QtCore.QRect(110, 160, 181, 31))
        self.birth.setObjectName("birth")
        self.id = QtWidgets.QTextEdit(zhuce)
        self.id.setGeometry(QtCore.QRect(110, 220, 181, 31))
        self.id.setObjectName("id")
        self.password = QtWidgets.QTextEdit(zhuce)
        self.password.setGeometry(QtCore.QRect(110, 280, 181, 31))
        self.password.setObjectName("password")

        self.retranslateUi(zhuce)
        self.pushButton_3.clicked.connect(self.tuichu)
        self.pushButton.clicked.connect(self.wancheng)
        self.pushButton_2.clicked.connect(self.gerenjingli)
        QtCore.QMetaObject.connectSlotsByName(zhuce)

    def retranslateUi(self, zhuce):
        _translate = QtCore.QCoreApplication.translate
        zhuce.setWindowTitle(_translate("zhuce", "注册"))
        self.label.setText(_translate("zhuce", "姓名"))
        self.label_2.setText(_translate("zhuce", "性别"))
        self.label_3.setText(_translate("zhuce", "生日"))
        self.label_4.setText(_translate("zhuce", "账号"))
        self.label_5.setText(_translate("zhuce", "密码"))
        self.pushButton.setText(_translate("zhuce", "完成"))
        self.pushButton_2.setText(_translate("zhuce", "添加个人经历"))
        self.pushButton_3.setText(_translate("zhuce", "退出"))

import picture_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_zhuce()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())