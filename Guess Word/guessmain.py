import sys
import time
from guess import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.addItems("4 5".split())
        self.label = QtWidgets.QLabel("@ Andrey Volkov, 2019")
        self.ui.statusbar.addWidget(self.label)

        self.ui.pushButton.clicked.connect(self.start1)
        self.ui.pushButton_2.clicked.connect(self.saveToFile)

        self.writeFile = open("text.txt", "w",  encoding='utf-8')
        self.writeFile.close()

    def start1(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.plainTextEdit.clear()

        if self.ui.comboBox.currentIndex() == 0:
            self.wordFour(self.ui.lineEdit.text())
        elif self.ui.comboBox.currentIndex() == 1:
            self.wordFive(self.ui.lineEdit.text())

    def saveToFile(self):
        self.writeFile = open("text.txt", "a",  encoding='utf-8')
        self.writeFile.write("Ввод: %s\n" %self.ui.lineEdit.text())
        self.writeFile.write(self.ui.plainTextEdit.toPlainText())
        self.writeFile.write("\n\n")
        self.writeFile.close()
        self.ui.statusbar.showMessage("Content Saved", 3000)


    def wordFour(self, letters):
        self.cancelled = False

        self.t1 = time.time()
        self.c = 0
        self.resArr = []
        self.initW = letters
        self.res = ["", "", "", ""]
        self.r = open("dict.txt", "r")
        self.fileRead = self.r.read()
        self.fileSplit0 = self.fileRead.split()
        self.fileSplit = []
        for word in self.fileSplit0:
            if len(word) == 4:
                self.fileSplit.append(word)
        self.r.close()

        self.progress = QtWidgets.QProgressDialog("Searching...", "Stop", 0, len(self.initW), self.ui.lineEdit)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setMinimumDuration(1000)


        for self.i in range(0, len(self.initW)):
            self.res[0] = self.initW[self.i]

            self.progress.setValue(self.i)
            if self.progress.wasCanceled():
                self.cancelled = True
                return

            for self.q in range(0, len(self.initW)):
                if (self.q != self.i):
                    self.res[1] = self.initW[self.q]

                    for self.p in range(0, len(self.initW)):
                        if(self.p != self.i) and (self.p != self.q):
                            self.res[2] = self.initW[self.p]

                            for self.pp in range(0, len(self.initW)):
                                if (self.pp != self.i) and (self.pp != self.q) and (self.pp != self.p):
                                    self.res[3] = self.initW[self.pp]
                                    self.wordFor = self.res[0] + self.res[1] + self.res[2] + self.res[3]
                                    if self.wordFor in self.fileSplit:
                                        if self.wordFor not in self.resArr:
                                            self.resArr.append(self.wordFor)
                                    self.c += 1
        self.str = "Найдено совпадений: " + str(len(self.resArr)) + "\n" + self.arrOutput(self.resArr) + \
                   "\n" + str(self.c) + " комбинаций проверено\nВремя исполнения: " + str(time.time() - self.t1) + " c."
        self.ui.plainTextEdit.appendPlainText(self.str)
        self.progress.deleteLater()

        self.ui.pushButton.setEnabled(True)


    def wordFive(self, letters):
        self.cancelled = False

        self.t1 = time.time()
        self.c = 0
        self.resArr = []
        self.initW = letters
        self.res = ["", "", "", "", ""]
        self.r = open("dict.txt", "r")
        self.fileRead = self.r.read()
        self.fileSplit0 = self.fileRead.split()
        self.fileSplit = []
        for word in self.fileSplit0:
            if len(word) == 5:
                self.fileSplit.append(word)
        self.r.close()

        self.progress = QtWidgets.QProgressDialog("Searching...", "Stop", 0, len(self.initW), self.ui.lineEdit)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setMinimumDuration(1000)

        for self.i in range(0, len(self.initW)):
            self.res[0] = self.initW[self.i]

            self.progress.setValue(self.i)
            if self.progress.wasCanceled():
                self.cancelled = True
                return

            for self.q in range(0, len(self.initW)):
                if (self.q != self.i):
                    self.res[1] = self.initW[self.q]

                    for self.p in range(0, len(self.initW)):
                        if (self.p != self.i) and (self.p != self.q):
                            self.res[2] = self.initW[self.p]

                            for self.pp in range(0, len(self.initW)):
                                if (self.pp != self.i) and (self.pp != self.q) and (self.pp != self.p):
                                    self.res[3] = self.initW[self.pp]

                                    for self.qq in range(0, len(self.initW)):
                                        if (self.qq != self.i) and (self.qq != self.q) and (self.qq != self.p) and (self.qq != self.pp):
                                            self.res[4] = self.initW[self.qq]
                                            self.wordFor = self.res[0] + self.res[1] + self.res[2] + self.res[3] + self.res[4]
                                            if self.wordFor in self.fileSplit:
                                                if self.wordFor not in self.resArr:
                                                    self.resArr.append(self.wordFor)
                                            self.c += 1
        self.str = "Найдено совпадений: " + str(len(self.resArr)) + "\n" + self.arrOutput(self.resArr) + \
                   "\n" + str(self.c) + " комбинаций проверено\nВремя исполнения: " + str(time.time() - self.t1) + " с."
        self.ui.plainTextEdit.appendPlainText(self.str)
        self.progress.deleteLater()

        self.ui.pushButton.setEnabled(True)

    def arrOutput(self, arr):
        arr.sort()
        self.str = ""
        for i in range(0, len(arr)):
            if i != len(arr) - 1:
                self.str += arr[i] + ", "
            else:
                self.str += arr[i] + "."
        return self.str



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())