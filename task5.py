import re
import string
from PyQt5 import QtCore, QtGui, QtWidgets

class StringFormatter(object):
    def __init__(self, str):
        re.sub(r'[^\w\s]', '', str)
        self.str = str

    def DelWords(self, n):
        words = self.str.split(" ")
        result = []
        for word in words:
            if len(word) >= n:
                result.append(word)
        self.str = " ".join(result)

    def replaceNumbers(self):
        result = re.sub('\d', '*', self.str)
        self.str = result

    def addSpace(self):
        result = " ".join(self.str)
        self.str = result

    def sortWords(self):
        sortWords = self.str.split(" ")
        sortWords.sort(key=lambda item: (-len(item), item))
        self.str = " ".join(sortWords)

    def alphabetSort(self):
        result = sorted(self.str.split(' '))
        self.str = " ".join(result)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 91, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 490, 81, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 661, 22))
        self.lineEdit.setObjectName("str")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 500, 661, 22))
        self.lineEdit_2.setObjectName("Result")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(120, 70, 221, 20))
        self.checkBox.setObjectName("DelWords")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(350, 70, 51, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 70, 55, 21))
        self.label_3.setObjectName("label_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 110, 181, 20))
        self.checkBox_2.setObjectName("ReplaceNum")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(120, 150, 261, 20))
        self.checkBox_3.setObjectName("AddSpace")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(120, 190, 151, 20))
        self.checkBox_4.setObjectName("Sort")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(170, 220, 101, 20))
        self.radioButton.setObjectName("LenWords")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 260, 151, 20))
        self.radioButton_2.setObjectName("Lec")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(122, 310, 641, 151))
        self.pushButton.setObjectName("Start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if self.checkBox_4.checkState() == 0:
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)

        self.checkBox_4.clicked.connect(self.CheckStatus)
        self.pushButton.clicked.connect(self.Start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StringFormatter"))
        self.label.setText(_translate("MainWindow", "Строка:"))
        self.label_2.setText(_translate("MainWindow", "Результат:"))
        self.checkBox.setText(_translate("MainWindow", "Удалить слова размером меньше"))
        self.label_3.setText(_translate("MainWindow", "букв"))
        self.checkBox_2.setText(_translate("MainWindow", "Заменить все цифры на *"))
        self.checkBox_3.setText(_translate("MainWindow", "Добавить пробелы между символами"))
        self.checkBox_4.setText(_translate("MainWindow", "Сортировать слова:"))
        self.radioButton.setText(_translate("MainWindow", "По размеру"))
        self.radioButton_2.setText(_translate("MainWindow", "Лексикографически"))
        self.pushButton.setText(_translate("MainWindow", "Форматировать"))

    def Start(self):
        f = StringFormatter(self.lineEdit.text())
        if(self.checkBox.checkState() != 0):
            f.DelWords(int(self.spinBox.text()))

        if(self.checkBox_2.checkState() != 0):
            f.replaceNumbers()

        if (self.checkBox_4.checkState() != 0):
            if (self.radioButton.isChecked()):
                f.sortWords()
            elif (self.radioButton_2.isChecked()):
                f.alphabetSort()
            else:
                pass

        if(self.checkBox_3.checkState() != 0):
            f.addSpace()

        self.lineEdit_2.setText(f.str)

    def CheckStatus(self):
        if self.checkBox_4.checkState() == 0:
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
        elif self.checkBox_4.checkState() != 0:
            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
