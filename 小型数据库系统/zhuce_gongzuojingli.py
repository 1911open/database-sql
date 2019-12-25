# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce_gongzuojingli.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import zhuce_gerenjingli
import pymysql


def regisster(work,time,job):
    try:
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='201314xIn', db='sz160110115', charset='utf8')
        cursor = db.cursor()
        sql = "select * from we where id in (select id from new_table where time in (select MAX(time) from new_table))"
        cursor.execute(sql)
        data = cursor.fetchall()
        name = data[0][3]
        id = data[0][4]
        sql = "replace into we(work,time,job,name,id) values (%s,%s,%s,%s,%s)"
        res = [work, time, job, name, id]
        cursor.execute(sql, res)
        print(cursor.fetchall())
        db.commit()
        cursor.close()
        db.close()
    except:
        pass

class Ui_Form(object):
    def save(self):
        work = self.work.toPlainText()
        time = self.time.toPlainText()
        job = self.job.toPlainText()
        regisster(work,time,job)
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
        self.work = QtWidgets.QTextEdit(Form)
        self.work.setGeometry(QtCore.QRect(110, 40, 211, 31))
        self.work.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.work.setObjectName("work")
        self.time = QtWidgets.QTextEdit(Form)
        self.time.setGeometry(QtCore.QRect(110, 100, 211, 31))
        self.time.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.time.setObjectName("time")
        self.job = QtWidgets.QTextEdit(Form)
        self.job.setGeometry(QtCore.QRect(110, 160, 211, 31))
        self.job.setStyleSheet("border-image: url(:/res/white.jpg);\n"
"border-image: url(:/res/pink.jpg);")
        self.job.setObjectName("job")
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
        self.label.setText(_translate("Form", "工作地点"))
        self.label_2.setText(_translate("Form", "工作时间"))
        self.label_3.setText(_translate("Form", "职业"))
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