import os
import re
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QListView, QApplication, QWidget, QVBoxLayout, QLabel, QMessageBox, QInputDialog, \
    QFileDialog, QDialog, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


class VLine(QFrame):
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine | self.Sunken)

class HomePage(QDialog):
    def __init__(self):
        super(HomePage, self).__init__()
        loadUi('HomePage.ui', self)
        self.btnLoginPage.clicked.connect(self.executeLoginPage)
        self.btnRegisterPage.clicked.connect(self.executeRegisterPage)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 771, 521))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Log = QtWidgets.QMenu(self.menubar)
        self.Log.setObjectName("Log")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.addPermanentWidget(VLine())
        MainWindow.setStatusBar(self.statusbar)
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Export = QtWidgets.QAction(MainWindow)
        self.Export.setObjectName("Export")
        self.AddLog = QtWidgets.QAction(MainWindow)
        self.AddLog.setObjectName("AddLog")
        self.ShowLog = QtWidgets.QAction(MainWindow)
        self.ShowLog.setObjectName("ShowLog")
        self.File.addAction(self.Open)
        self.Log.addAction(self.Export)
        self.Log.addAction(self.AddLog)
        self.Log.addAction(self.ShowLog)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Log.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Open.triggered.connect(self.open)

        self.Export.triggered.connect(lambda: self.export(QFileDialog.getOpenFileNames()[0][0]))
        self.AddLog.triggered.connect(lambda: self.export("script18.log"))
        self.ShowLog.triggered.connect(self.showLog)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск строк"))
        self.File.setTitle(_translate("MainWindow", "Файл"))
        self.Log.setTitle(_translate("MainWindow", "Лог"))
        self.Open.setText(_translate("MainWindow", "Открыть"))
        self.Export.setText(_translate("MainWindow", "Экспорт"))
        self.AddLog.setText(_translate("MainWindow", "Добавить в Лог"))
        self.ShowLog.setText(_translate("MainWindow", "Просмотр"))

    def showLog(self):
        if os.path.exists("script18.log"):
            ok = self.show_question_messagebox()
            if ok == 1024:
                self.statusbar.showMessage("Открыт лог")
                self.listWidget.clear()
                file = open("script18.log", "r")
                lines = file.readlines()
                file.close()

                for i in lines:
                    if (i != "" and i != "\n"):
                        self.listWidget.addItem(i)
        else:
            self.show_info_messagebox()
            f = open("script18.log", "x")

    def export(self, nameLog):
        try:
            if os.path.exists(nameLog):
                file = open(nameLog, "a")
                for x in range(self.listWidget.count()):
                    file.write(str(f"\n{self.listWidget.item(x).text()}"))
                file.close()
            else:
                self.show_info_messagebox()
                f = open("script18.log", "x")
        except: pass

    def open(self):
        try:
            fileName = QFileDialog.getOpenFileNames()[0][0]
            self.statusbar.showMessage(f"Обработан файл {fileName}")
            self.label_for_statusbur = QLabel(f"{os.path.getsize(fileName)} байт")
            self.statusbar.addPermanentWidget(self.label_for_statusbur)
            dt_now = datetime.datetime.now().time()
            it = f"\nФайл {fileName}, был отработан {dt_now} \n"
            self.listWidget.addItem(it)
            file = open(fileName, "r", encoding="utf-8")
            lines = file.readlines()
            file.close()
        except: pass

        pattern =r"(int|short|byte)\s+([a-zA-Z_]\w*)\s*=\s*(-?\d+)\s"

        for i in range(len(lines)):
            for j in re.findall(pattern, lines[i]):
                if j != None:
                    it = f"Строка: {i + 1} | Позиция: {lines[i].find(j[0]) + 1} | Найдено: {j[0]} {j[1]} = {j[2]}"
                    self.listWidget.addItem(it)

    def statusBarMessege(self):
        self.statusbar.showMessage('Message in statusbar.')

    def add_function(self):
        self.statusBarMessege()

    def show_info_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Файл диалога не найден и будет создан автоматически.")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def show_question_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Текущий список будет удалён. Вы уверены что хотите открыть лог?")
        msg.setWindowTitle("Question")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        return retval


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
