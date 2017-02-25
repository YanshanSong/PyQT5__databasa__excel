# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\witch\Desktop\hospital\main2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main2Window(object):
    def setupUi(self, Main2Window):
        Main2Window.setObjectName("Main2Window")
        Main2Window.resize(470, 508)
        self.centralWidget = QtWidgets.QWidget(Main2Window)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(63, 20, 51, 20))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 40, 351, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(63, 230, 51, 20))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 250, 351, 181))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 440, 351, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        Main2Window.setCentralWidget(self.centralWidget)

        self.retranslateUi(Main2Window)
        QtCore.QMetaObject.connectSlotsByName(Main2Window)

    def retranslateUi(self, Main2Window):
        _translate = QtCore.QCoreApplication.translate
        Main2Window.setWindowTitle(_translate("Main2Window", "数据库导出"))
        self.label.setText(_translate("Main2Window", "数据表"))
        self.label_2.setText(_translate("Main2Window", "excel表"))
        self.label_3.setText(_translate("Main2Window", "保存地址: "))
        self.toolButton.setText(_translate("Main2Window", "..."))
        self.pushButton.setText(_translate("Main2Window", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main2Window = QtWidgets.QMainWindow()
    ui = Ui_Main2Window()
    ui.setupUi(Main2Window)
    Main2Window.show()
    sys.exit(app.exec_())

