# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmartCal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import zip_longest
from PyQt5.QtGui import QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(781, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFontPointSize(15)
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.push1Button = QtWidgets.QPushButton(self.centralwidget)
        self.push1Button.setObjectName("push1Button")
        self.push1Button.clicked.connect(self.click1)
        self.horizontalLayout.addWidget(self.push1Button)
        self.push2Button = QtWidgets.QPushButton(self.centralwidget)
        self.push2Button.setObjectName("push2Button")
        self.push2Button.clicked.connect(self.click2)
        self.horizontalLayout.addWidget(self.push2Button)
        self.push3Button = QtWidgets.QPushButton(self.centralwidget)
        self.push3Button.setObjectName("push3Button")
        self.push3Button.clicked.connect(self.click3)
        self.horizontalLayout.addWidget(self.push3Button)
        self.pushPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushPlusButton.setObjectName("pushPlusButton")
        self.pushPlusButton.clicked.connect(self.clickPlus)
        self.horizontalLayout.addWidget(self.pushPlusButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push4Button = QtWidgets.QPushButton(self.centralwidget)
        self.push4Button.setObjectName("push4Button")
        self.push4Button.clicked.connect(self.click4)
        self.horizontalLayout_2.addWidget(self.push4Button)
        self.push5Button = QtWidgets.QPushButton(self.centralwidget)
        self.push5Button.setObjectName("push5Button")
        self.push5Button.clicked.connect(self.click5)
        self.horizontalLayout_2.addWidget(self.push5Button)
        self.push6Button = QtWidgets.QPushButton(self.centralwidget)
        self.push6Button.setObjectName("push6Button")
        self.push6Button.clicked.connect(self.click6)
        self.horizontalLayout_2.addWidget(self.push6Button)
        self.pushMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushMinusButton.setObjectName("pushMinusButton")
        self.pushMinusButton.clicked.connect(self.clickMinus)
        self.horizontalLayout_2.addWidget(self.pushMinusButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.push7Button = QtWidgets.QPushButton(self.centralwidget)
        self.push7Button.setObjectName("push7Button")
        self.push7Button.clicked.connect(self.click7)
        self.horizontalLayout_3.addWidget(self.push7Button)
        self.push8Button = QtWidgets.QPushButton(self.centralwidget)
        self.push8Button.setObjectName("push8Button")
        self.push8Button.clicked.connect(self.click8)
        self.horizontalLayout_3.addWidget(self.push8Button)
        self.push9Button = QtWidgets.QPushButton(self.centralwidget)
        self.push9Button.setObjectName("push9Button")
        self.push9Button.clicked.connect(self.click9)
        self.horizontalLayout_3.addWidget(self.push9Button)
        self.pushMultiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushMultiplyButton.setObjectName("pushMultiplyButton")
        self.pushMultiplyButton.clicked.connect(self.clickMultiply)
        self.horizontalLayout_3.addWidget(self.pushMultiplyButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushStartoverButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushStartoverButton.setObjectName("pushStartoverButton")
        self.pushStartoverButton.clicked.connect(self.StartOver)
        self.horizontalLayout_4.addWidget(self.pushStartoverButton)
        self.push0Button = QtWidgets.QPushButton(self.centralwidget)
        self.push0Button.setObjectName("push0Button")
        self.push0Button.clicked.connect(self.click0)
        self.horizontalLayout_4.addWidget(self.push0Button)
        self.pushBackspaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushBackspaceButton.setObjectName("pushBackspaceButton")
        self.horizontalLayout_4.addWidget(self.pushBackspaceButton)
        self.pushDivideButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushDivideButton.setObjectName("pushDivideButton")
        self.pushDivideButton.clicked.connect(self.clickDivide)
        self.horizontalLayout_4.addWidget(self.pushDivideButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushCalculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushCalculateButton.setObjectName("pushCalculateButton")
        self.pushCalculateButton.clicked.connect(self.clickCalculate)
        self.verticalLayout.addWidget(self.pushCalculateButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.triggered.connect(self.Aboutclicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SmartCal"))
        self.push1Button.setText(_translate("MainWindow", "1"))
        self.push1Button.setShortcut(_translate("MainWindow", "1"))
        self.push2Button.setText(_translate("MainWindow", "2"))
        self.push2Button.setShortcut(_translate("MainWindow", "2"))
        self.push3Button.setText(_translate("MainWindow", "3"))
        self.push3Button.setShortcut(_translate("MainWindow", "3"))
        self.pushPlusButton.setText(_translate("MainWindow", "+"))
        self.pushPlusButton.setShortcut(_translate("MainWindow", "+"))
        self.push4Button.setText(_translate("MainWindow", "4"))
        self.push4Button.setShortcut(_translate("MainWindow", "4"))
        self.push5Button.setText(_translate("MainWindow", "5"))
        self.push5Button.setShortcut(_translate("MainWindow", "5"))
        self.push6Button.setText(_translate("MainWindow", "6"))
        self.push6Button.setShortcut(_translate("MainWindow", "6"))
        self.pushMinusButton.setText(_translate("MainWindow", "-"))
        self.pushMinusButton.setShortcut(_translate("MainWindow", "-"))
        self.push7Button.setText(_translate("MainWindow", "7"))
        self.push7Button.setShortcut(_translate("MainWindow", "7"))
        self.push8Button.setText(_translate("MainWindow", "8"))
        self.push8Button.setShortcut(_translate("MainWindow", "8"))
        self.push9Button.setText(_translate("MainWindow", "9"))
        self.push9Button.setShortcut(_translate("MainWindow", "9"))
        self.pushMultiplyButton.setText(_translate("MainWindow", "*"))
        self.pushMultiplyButton.setShortcut(_translate("MainWindow", "*"))
        self.pushStartoverButton.setText(_translate("MainWindow", "Start Over"))
        self.pushStartoverButton.setShortcut(_translate("MainWindow", "Esc"))
        self.push0Button.setText(_translate("MainWindow", "0"))
        self.push0Button.setShortcut(_translate("MainWindow", "0"))
        self.pushBackspaceButton.setText(_translate("MainWindow", "Backspace"))
        self.pushBackspaceButton.setShortcut(_translate("MainWindow", "Backspace"))
        self.pushBackspaceButton.clicked.connect(self.Backspace)
        self.pushDivideButton.setText(_translate("MainWindow", "/"))
        self.pushDivideButton.setShortcut(_translate("MainWindow", "/"))
        self.pushCalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.pushCalculateButton.setShortcut(_translate("MainWindow", "Return"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def click0(self):
        self.textBrowser.insertPlainText("0")

    def click1(self):
        self.textBrowser.insertPlainText("1")

    def click2(self):
        self.textBrowser.insertPlainText("2")

    def click3(self):
        self.textBrowser.insertPlainText("3")

    def click4(self):
        self.textBrowser.insertPlainText("4")

    def click5(self):
        self.textBrowser.insertPlainText("5")

    def click6(self):
        self.textBrowser.insertPlainText("6")

    def click7(self):
        self.textBrowser.insertPlainText("7")
    
    def click8(self):
        self.textBrowser.insertPlainText("8")

    def click9(self):
        self.textBrowser.insertPlainText("9")

    def clickPlus(self):
        self.textBrowser.append("+")
        self.textBrowser.append("")

    def clickMinus(self):
        self.textBrowser.append("-")
        self.textBrowser.append("")
    
    def clickMultiply(self):
        self.textBrowser.append("*")
        self.textBrowser.append("")
    
    def clickDivide(self):
        self.textBrowser.append("/")
        self.textBrowser.append("")

    def StartOver(self):
        self.textBrowser.clear()
        self.textBrowser.setFontPointSize(15)
        self.textBrowser.setTextColor(QColor(0,0,0))

    def Backspace(self):
        self.currentString = self.textBrowser.toPlainText()
        self.outputString = self.currentString[0:len(self.currentString)-1]
        self.textBrowser.clear()
        self.textBrowser.insertPlainText(self.outputString)

    def clickCalculate(self):
        self.inputString = self.textBrowser.toPlainText()
        if(self.inputString.find("+")!=-1):
            self.operand1 = self.inputString.split('+')[0].rstrip()
            self.operand2 = self.inputString.split('+')[1].lstrip()
            res = self.add()
        if(self.inputString.find("-")!=-1):
            self.operand1 = self.inputString.split('-')[0].rstrip()
            self.operand2 = self.inputString.split('-')[1].lstrip()
            res = self.minus()
        if(self.inputString.find("*")!=-1):
            self.operand1 = self.inputString.split('*')[0].rstrip()
            self.operand2 = self.inputString.split('*')[1].lstrip()
            res = self.multiply()
        if(self.inputString.find("/")!=-1):
            self.operand1 = self.inputString.split('/')[0].rstrip()
            self.operand2 = self.inputString.split('/')[1].lstrip()
            res = self.divide()
        self.textBrowser.clear()
        self.textBrowser.setTextColor(QColor(0,255,0))
        self.textBrowser.setFontPointSize(30)
        self.textBrowser.setText(res)

    def Aboutclicked(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_About()
        self.ui.setupUi(self.window)
        self.window.show()

    def add(self):
        a=list(self.operand1[::-1])
        b=list(self.operand2[::-1])
        carry = 0
        finalsum = ""
        for (val1,val2) in zip_longest(a,b):
                if val1 != None and val2 != None:
                    tempsum = int(val1) + int(val2) + carry
                    if len(str(tempsum))==2:
                        carry = int(str(tempsum)[0])
                        finalsum = finalsum+str(tempsum)[1]
                    else:
                        finalsum = finalsum+str(tempsum)[0]
                elif val1!=None and val2 == None:
                    s = int(val1) + carry
                    finalsum = finalsum+str(s)
                    carry = 0
                elif val1==None and val2!=None:
                    s = int(val2) + carry
                    finalsum = finalsum+str(s)
                    carry = 0
        if carry != 0:
            finalsum = finalsum + str(carry)
        return(finalsum[::-1])

    def minus(self):
        a = self.operand1[::-1]
        b = self.operand2[::-1]
        carry = 0
        finalsum = ""
        if(len(a)>len(b)):
            for(val1,val2) in zip_longest(a,b):
                if carry == 1:
                    val1 = str(int(val1)-1)
                    carry = 0
                if val1!=None and val2 !=None and val1>val2:
                    tempsum = int(val1)-int(val2)
                elif val1!=None and val2!=None and val1<val2:
                    tempsum = 10+int(val1)-int(val2)
                    carry = 1
                elif val1==val2:
                    tempsum=0
                elif val1!=None and val2==None:
                    tempsum = int(val1)
                finalsum = finalsum+str(tempsum)
        if(len(a)<len(b)):
            for(val1,val2) in zip_longest(b,a):
                if carry == 1:
                    val1 = str(int(val1)-1)
                    carry = 0
                if val1!=None and val2 !=None and val1>val2:
                    tempsum = int(val1)-int(val2)
                elif val1!=None and val2!=None and val1<val2:
                    tempsum = 10+int(val1)-int(val2)
                    carry = 1
                elif val1==val2:
                    tempsum = 0
                elif val1!=None and val2==None:
                    tempsum = int(val1)
                finalsum = finalsum+str(tempsum)
            finalsum = finalsum + "-"
        if(len(a)==len(b)):
            if(int(a[len(a)-1]) < int(b[len(a)-1])):
                for(val1,val2) in zip_longest(b,a):
                    if carry == 1:
                        val1 = str(int(val1)-1)
                        carry = 0
                    if val1!=None and val2 !=None and val1>val2:
                        tempsum = int(val1)-int(val2)
                    elif val1!=None and val2!=None and val1<val2:
                        tempsum = 10+int(val1)-int(val2)
                        carry = 1
                    elif val1==val2:
                        tempsum=0
                    elif val1!=None and val2==None:
                        tempsum = int(val1)
                    finalsum = finalsum+str(tempsum)
                finalsum = finalsum + "-"
            if(int(a[len(a)-1]) > int(b[len(a)-1])):
                for(val1,val2) in zip_longest(a,b):
                    if carry == 1:
                        val1 = str(int(val1)-1)
                        carry = 0
                    if val1!=None and val2 !=None and val1>val2:
                        tempsum = int(val1)-int(val2)
                    elif val1!=None and val2!=None and val1<val2:
                        tempsum = 10+int(val1)-int(val2)
                        carry = 1
                    elif val1==val2:
                        tempsum=0
                    elif val1!=None and val2==None:
                        tempsum = int(val1)
                    finalsum = finalsum+str(tempsum)
        return finalsum[::-1]

    def multiply(self):
        a = self.operand1
        b = self.operand2
        return str(int(a) * int(b))

    def divide(self):
        a = self.operand1
        b = self.operand2
        if(int(b)!=0):
            return str(int(a)/int(b))
        else:
            error_message = QtWidgets.QErrorMessage()
            error_message.setWindowTitle("Error!")
            error_message.showMessage("Cannot divide by 0")
            error_message.exec()
        
class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(362, 314)
        self.gridLayout = QtWidgets.QGridLayout(About)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(About)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Form"))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">SmartCal is free to use software developed by Atul Gupta. The unique attribute about SmartCal is that it is capable of performing operations on any length of numbers.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">This is a work in development and I am looking for contributors to further enhance the project.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
