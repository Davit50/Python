from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import finish


class main(object):
    def main(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.setGeometry(QtCore.QRect(-1, -1, 1920, 1080))
        SecondWindow.setFixedSize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 200, 301, 231))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 200, 301, 231))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.pushButton.setText("exit")
        self.pushButton_2.setText("finish")

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.finish)

    def close(self):
        QCoreApplication.quit()
    def finish(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = finish.finish()
        self.ui.finish(self.window)
        self.window.show()
        # SecondWindow.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = main()
    ui.main(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
