from PyQt5 import QtCore, QtGui, QtWidgets
import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(-1, -1, 1920, 1080))
        MainWindow.setFixedSize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(573, 191, 774, 88))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FF9E9E;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(556, 357, 384, 143))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("color: #FFFFFF;background: #FF9E9E;\n"
                                "border-top-left-radius: 25px;\n"
                                "")
        self.btn1.setObjectName("btn1")

        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(980, 357, 384, 143))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("color: #FFFFFF;background: #FF9E9E;\n"
                                "border-top-right-radius: 25px;\n"
                                "")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(556, 540, 384, 143))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("color: #FFFFFF;background: #FF9E9E;\n"
                                "border-bottom-left-radius: 25px;\n"
                                "")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(980, 540, 384, 143))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("color: #FFFFFF;background: #FF9E9E;\n"
                                "border-bottom-right-radius: 25px;\n"
                                "")
        self.btn4.setObjectName("btn4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(-2000, -2000, 4000, 4000))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_14.lower()

        self.label.setText("ԸՆՏՐԵԼ ԱՌԱՐԿԱՆ")
        self.btn1.setText("ՊԱՏՄ")
        self.btn2.setText("ՖԻԶԻԿԱ")
        self.btn3.setText("ՄԱԹԵՄ")
        self.btn4.setText("ԼԵԶՈՒՆԵՐ")

        self.btn1.clicked.connect(self.main1)
        self.btn2.clicked.connect(self.main1)
        self.btn3.clicked.connect(self.main1)
        self.btn4.clicked.connect(self.main1)

    def main1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.main()
        self.ui.main(self.window)
        self.window.show()
        # MainWindow.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
