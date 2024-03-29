# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 460)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setToolTipDuration(1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(0, 60, 100, 100))
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(100, 60, 100, 100))
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(200, 60, 100, 100))
        self.b9.setObjectName("b9")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(100, 160, 100, 100))
        self.b5.setObjectName("b5")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(0, 160, 100, 100))
        self.b4.setObjectName("b4")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(200, 160, 100, 100))
        self.b6.setObjectName("b6")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(100, 260, 100, 100))
        self.b2.setObjectName("b2")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(0, 260, 100, 100))
        self.b1.setObjectName("b1")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(200, 260, 100, 100))
        self.b3.setObjectName("b3")
        self.sub = QtWidgets.QPushButton(self.centralwidget)
        self.sub.setGeometry(QtCore.QRect(300, 160, 100, 100))
        self.sub.setObjectName("sub")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(100, 360, 200, 100))
        self.equal.setObjectName("equal")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(300, 60, 100, 100))
        self.add.setObjectName("add")
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(0, 360, 100, 100))
        self.b0.setObjectName("b0")
        self.mul = QtWidgets.QPushButton(self.centralwidget)
        self.mul.setGeometry(QtCore.QRect(300, 260, 100, 100))
        self.mul.setObjectName("mul")
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(300, 360, 100, 100))
        self.div.setObjectName("div")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 61))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                 "background-color: rgb(69, 80, 73);\n"
                                 "background-color: rgb(157, 157, 157);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 12pt \"MS Shell Dlg 2\";\n"
                                 "direction:rtl;\n"
                                 "")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.equal.setText(_translate("MainWindow", "="))
        self.sub.setText(_translate("MainWindow", "-"))
        self.add.setText(_translate("MainWindow", "+"))
        self.mul.setText(_translate("MainWindow", "*"))
        self.div.setText(_translate("MainWindow", "/"))

        self.label.setText(_translate("MainWindow", "0"))

    def add_functions(self):
        self.b0.clicked.connect(lambda: self.write_number(self.b0.text()))
        self.b1.clicked.connect(lambda: self.write_number(self.b1.text()))
        self.b2.clicked.connect(lambda: self.write_number(self.b2.text()))
        self.b3.clicked.connect(lambda: self.write_number(self.b3.text()))
        self.b4.clicked.connect(lambda: self.write_number(self.b4.text()))
        self.b5.clicked.connect(lambda: self.write_number(self.b5.text()))
        self.b6.clicked.connect(lambda: self.write_number(self.b6.text()))
        self.b7.clicked.connect(lambda: self.write_number(self.b7.text()))
        self.b8.clicked.connect(lambda: self.write_number(self.b8.text()))
        self.b9.clicked.connect(lambda: self.write_number(self.b9.text()))
        self.add.clicked.connect(lambda: self.write_number(self.add.text()))
        self.sub.clicked.connect(lambda: self.write_number(self.sub.text()))
        self.mul.clicked.connect(lambda: self.write_number(self.mul.text()))
        self.div.clicked.connect(lambda: self.write_number(self.div.text()))
        self.equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label.text() == '0' or self.is_equal:
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        res = eval(self.label.text())
        self.label.setText('result: ' + str(res))
        self.is_equal = True


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
