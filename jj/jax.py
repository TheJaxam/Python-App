# Form implementation generated from reading ui file 'caculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
SET = ""
class Ui_Calculator(object):
    
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(318, 450)
        self.lineEdit = QtWidgets.QLineEdit(parent=Calculator)
        self.lineEdit.setGeometry(QtCore.QRect(10, 15, 298, 70))
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.Zero = QtWidgets.QPushButton(parent=Calculator)
        self.Zero.setGeometry(QtCore.QRect(10, 375, 220, 65))
        self.Zero.setObjectName("Zero")
        self.Zero.clicked.connect(self.ZERO)
        self.Seven = QtWidgets.QPushButton(parent=Calculator)
        self.Seven.setGeometry(QtCore.QRect(10, 305, 65, 65))
        self.Seven.setObjectName("Seven")
        self.Seven.clicked.connect(self.SEVEN)
        self.Eight = QtWidgets.QPushButton(parent=Calculator)
        self.Eight.setGeometry(QtCore.QRect(87, 305, 65, 65))
        self.Eight.setObjectName("Eight")
        self.Eight.clicked.connect(self.EIGHT)
        self.Nine = QtWidgets.QPushButton(parent=Calculator)
        self.Nine.setGeometry(QtCore.QRect(165, 305, 65, 65))
        self.Nine.setObjectName("Nine")
        self.Nine.clicked.connect(self.NINE)
        self.Six = QtWidgets.QPushButton(parent=Calculator)
        self.Six.setGeometry(QtCore.QRect(165, 235, 65, 65))
        self.Six.setObjectName("Six")
        self.Six.clicked.connect(self.SIX)
        self.Five = QtWidgets.QPushButton(parent=Calculator)
        self.Five.setGeometry(QtCore.QRect(87, 235, 65, 65))
        self.Five.setObjectName("Five")
        self.Five.clicked.connect(self.FIVE)
        self.Four = QtWidgets.QPushButton(parent=Calculator)
        self.Four.setGeometry(QtCore.QRect(10, 235, 65, 65))
        self.Four.setObjectName("Four")
        self.Four.clicked.connect(self.FOUR)
        self.Three = QtWidgets.QPushButton(parent=Calculator)
        self.Three.setGeometry(QtCore.QRect(165, 165, 65, 65))
        self.Three.setObjectName("Three")
        self.Three.clicked.connect(self.THREE)
        self.Tow = QtWidgets.QPushButton(parent=Calculator)
        self.Tow.setGeometry(QtCore.QRect(87, 165, 65, 65))
        self.Tow.setObjectName("Tow")
        self.Tow.clicked.connect(self.TOW)
        self.One = QtWidgets.QPushButton(parent=Calculator)
        self.One.setGeometry(QtCore.QRect(10, 165, 65, 65))
        self.One.setObjectName("One")
        self.One.clicked.connect(self.ONE)
        self.Clear_All = QtWidgets.QPushButton(parent=Calculator)
        self.Clear_All.setGeometry(QtCore.QRect(10, 105, 65, 50))
        self.Clear_All.setObjectName("Clear_All")
        self.Clear_All.clicked.connect(self.CLEAR_ALL)
        self.Clear_One = QtWidgets.QPushButton(parent=Calculator)
        self.Clear_One.setGeometry(QtCore.QRect(87, 105, 65, 50))
        self.Clear_One.setObjectName("Clear_One")
        self.Baghimande = QtWidgets.QPushButton(parent=Calculator)
        self.Baghimande.setGeometry(QtCore.QRect(165, 105, 65, 50))
        self.Baghimande.setObjectName("Baghimande")
        self.Baghimande.clicked.connect(self.BAGHIMANDE)
        self.Zarb = QtWidgets.QPushButton(parent=Calculator)
        self.Zarb.setGeometry(QtCore.QRect(243, 105, 65, 50))
        self.Zarb.setObjectName("Zarb")
        self.Zarb.clicked.connect(self.ZARB)
        self.Taghsim = QtWidgets.QPushButton(parent=Calculator)
        self.Taghsim.setGeometry(QtCore.QRect(243, 165, 65, 50))
        self.Taghsim.setObjectName("Taghsim")
        self.Taghsim.clicked.connect(self.TAGHSIM)
        self.Jam = QtWidgets.QPushButton(parent=Calculator)
        self.Jam.setGeometry(QtCore.QRect(243, 285, 65, 50))
        self.Jam.setObjectName("Jam")
        self.Jam.clicked.connect(self.JAM)
        self.Kasr = QtWidgets.QPushButton(parent=Calculator)
        self.Kasr.setGeometry(QtCore.QRect(243, 225, 65, 50))
        self.Kasr.setObjectName("Kasr")
        self.Kasr.clicked.connect(self.KASR)
        self.Mosavy = QtWidgets.QPushButton(parent=Calculator)
        self.Mosavy.setGeometry(QtCore.QRect(243, 345, 65, 95))
        self.Mosavy.setObjectName("Mosavy")
        self.Mosavy.clicked.connect(self.MOSAVY)

        
        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "JAX"))
        self.lineEdit.setText(_translate("Calculator", "0"))
        self.Zero.setText(_translate("Calculator", "0"))
        self.Seven.setText(_translate("Calculator", "7"))
        self.Eight.setText(_translate("Calculator", "8"))
        self.Nine.setText(_translate("Calculator", "9"))
        self.Six.setText(_translate("Calculator", "6"))
        self.Five.setText(_translate("Calculator", "5"))
        self.Four.setText(_translate("Calculator", "4"))
        self.Three.setText(_translate("Calculator", "3"))
        self.Tow.setText(_translate("Calculator", "2"))
        self.One.setText(_translate("Calculator", "1"))
        self.Clear_All.setText(_translate("Calculator", "CE"))
        self.Clear_One.setText(_translate("Calculator", "C"))
        self.Baghimande.setText(_translate("Calculator", "%"))
        self.Zarb.setText(_translate("Calculator", "×"))
        self.Taghsim.setText(_translate("Calculator", "÷"))
        self.Jam.setText(_translate("Calculator", "+"))
        self.Kasr.setText(_translate("Calculator", "-"))
        self.Mosavy.setText(_translate("Calculator", "="))

    
        
    
    def ZERO(self):
        global SET
        O_0 = self.Zero.text()
        SET+=O_0
        self.lineEdit.setText(str(SET))
        

    def ONE(self):
        global SET
        O_1 = self.One.text()
        SET+=O_1
        self.lineEdit.setText(str(SET))


    def TOW(self):
        global SET
        O_2 = self.Tow.text()
        SET+=O_2
        self.lineEdit.setText(str(SET))


    def THREE(self):
        global SET
        O_3 = self.Three.text()
        SET+=O_3
        self.lineEdit.setText(str(SET))


    def FOUR(self):
        global SET
        O_4 = self.Four.text()
        SET+=O_4
        self.lineEdit.setText(str(SET))


    def FIVE(self):
        global SET
        O_5 = self.Five.text()
        SET+=O_5
        self.lineEdit.setText(str(SET))


    def SIX(self):
        global SET
        O_6 = self.Six.text()
        SET+=O_6
        self.lineEdit.setText(str(SET))


    def SEVEN(self):
        global SET
        O_7 = self.Seven.text()
        SET+=O_7
        self.lineEdit.setText(str(SET))


    def EIGHT(self):
        global SET
        O_8 = self.Eight.text()
        SET+=O_8
        self.lineEdit.setText(str(SET))


    def NINE(self):
        global SET
        O_9 = self.Nine.text()
        SET+=O_9
        self.lineEdit.setText(str(SET))
    

    def JAM(self):
        global SET
        O_9 = self.Jam.text()
        SET+=O_9
        self.lineEdit.setText(str(SET))
    

    def KASR(self):
        global SET
        O_9 = self.Kasr.text()
        SET+=O_9
        self.lineEdit.setText(str(SET))
    

    def BAGHIMANDE(self):
        global SET
        O_9 = self.Baghimande.text()
        SET+=O_9
        self.lineEdit.setText(str(SET))


    def ZARB(self):
        global SET
        O_0 = "*"
        SET+=O_0
        self.lineEdit.setText(str(SET))


    def TAGHSIM(self):
        global SET
        O_0 = "//"
        SET+=O_0
        self.lineEdit.setText(str(SET))


    def CLEAR_ALL(self):
        global SET
        SET=""
        self.lineEdit.setText(str(SET))
        
    
    def MOSAVY(self):
        global SET
        SET=eval(SET)
        self.lineEdit.setText(str(SET))
        SET=str(SET)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QDialog()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec())
