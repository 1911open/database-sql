# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce_jiaoyujingli.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import zhuce_gerenjingli
import pymysql

def regisster(level,gdate,school,grade):
    try:
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='201314xIn', db='sz160110115', charset='utf8')
        cursor = db.cursor()
        sql = "select * from ee where id in (select id from new_table where time in (select MAX(time) from new_table))"
        cursor.execute(sql)
        data = cursor.fetchall()
        name = data[0][4]
        id = data[0][5]
        sql = "replace into ee(level,gdate,school,grade,name,id) values (%s,%s,%s,%s,%s,%s)"
        res = [level,gdate,school,grade,name,id]
        cursor.execute(sql, res)
        print(cursor.fetchall())
        db.commit()
        cursor.close()
        db.close()
    except:
        pass
class Ui_Form(object):

    def save(self):
        level = self.level.toPlainText()
        gdate = self.gdate.toPlainText()
        school = self.school.toPlainText()
        grade = self.grade.toPlainText()
        regisster(level,gdate,school,grade)
        self.form.close()
        Form3 = QtWidgets.QMainWindow()
        self.ui = zhuce_gerenjingli.Ui_gerenjingli()
        self.ui.setupUi(Form3)
        Form3.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 427)
        Form.setStyleSheet("border-image: url(:/res/flower.jpg);")
        self.form = Form
        self.level = QtWidgets.QTextEdit(Form)
        self.level.setGeometry(QtCore.QRect(110, 40, 211, 31))
        self.level.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.level.setObjectName("level")
        self.gdate = QtWidgets.QTextEdit(Form)
        self.gdate.setGeometry(QtCore.QRect(110, 100, 211, 31))
        self.gdate.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.gdate.setObjectName("gdate")
        self.school = QtWidgets.QTextEdit(Form)
        self.school.setGeometry(QtCore.QRect(110, 160, 211, 31))
        self.school.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.school.setObjectName("school")
        self.grade = QtWidgets.QTextEdit(Form)
        self.grade.setGeometry(QtCore.QRect(110, 220, 211, 31))
        self.grade.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.grade.setObjectName("grade")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 72, 31))
        self.label.setStyleSheet("font: 9pt \"幼圆\";;\n"
"color: rgb(255, 255, 0);\n"
"border-image: url(:/res/pink.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 72, 31))
        self.label_2.setStyleSheet("font: 9pt \"幼圆\";;\n"
"color: rgb(255, 255, 0);\n"
"border-image: url(:/res/pink.jpg);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 72, 31))
        self.label_3.setStyleSheet("font: 9pt \"幼圆\";;\n"
"color: rgb(255, 255, 0);\n"
"border-image: url(:/res/pink.jpg);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 72, 31))
        self.label_4.setStyleSheet("font: 9pt \"幼圆\";;\n"
"color: rgb(255, 255, 0);\n"
"border-image: url(:/res/pink.jpg);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 320, 93, 28))
        self.pushButton.setStyleSheet("font: 10pt \"幼圆\";\n"
"color: rgb(255, 0, 0);\n"
"background-image: url(:/res/pink.jpg);\n"
"border-image: url(:/res/pink.jpg);\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.save)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "教育水平"))
        self.label_2.setText(_translate("Form", "毕业日期"))
        self.label_3.setText(_translate("Form", "毕业院校"))
        self.label_4.setText(_translate("Form", "教育等级"))
        self.pushButton.setText(_translate("Form", "完成"))

import picture_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())