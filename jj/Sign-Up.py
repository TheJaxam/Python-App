from PyQt6 import QtCore, QtGui, QtWidgets
import json

class Ui_Sign_UP(object):
    def setupUi(self, Sign_UP):
        Sign_UP.setObjectName("Sign_UP")
        Sign_UP.setEnabled(True)
        Sign_UP.resize(342, 357)
        self.pushButton = QtWidgets.QPushButton(parent=Sign_UP)
        self.pushButton.setGeometry(QtCore.QRect(100, 270, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Sign_Up)
        self.UserName = QtWidgets.QLineEdit(parent=Sign_UP)
        self.UserName.setEnabled(True)
        self.UserName.setGeometry(QtCore.QRect(10, 60, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserName.sizePolicy().hasHeightForWidth())
        self.UserName.setSizePolicy(sizePolicy)
        self.UserName.setObjectName("UserName")
        self.UserName.setPlaceholderText("Write Your User Name")
        self.Password = QtWidgets.QLineEdit(parent=Sign_UP)
        self.Password.setEnabled(True)
        self.Password.setGeometry(QtCore.QRect(10, 130, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.Password.setObjectName("Password")
        self.Password.setPlaceholderText("Write Password")
        self.RePassword = QtWidgets.QLineEdit(parent=Sign_UP)
        self.RePassword.setEnabled(True)
        self.RePassword.setGeometry(QtCore.QRect(10, 200, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RePassword.sizePolicy().hasHeightForWidth())
        self.RePassword.setSizePolicy(sizePolicy)
        self.RePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.RePassword.setObjectName("RePassword")
        self.RePassword.setPlaceholderText("Write Password Again")
        self.label = QtWidgets.QLabel(parent=Sign_UP)
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Sign_UP)
        QtCore.QMetaObject.connectSlotsByName(Sign_UP)

    def retranslateUi(self, Sign_UP):
        _translate = QtCore.QCoreApplication.translate
        Sign_UP.setWindowTitle(_translate("Sign_UP", "Dialog"))
        self.pushButton.setText(_translate("Sign_UP", "Sign-Up"))
        self.label.setText(_translate("Sign_UP", "WELLCOME"))
    
    def Sign_Up(self):
        
        UserName = self.UserName.text()
        Password = self.Password.text()
        RePassword = self.RePassword.text()
        SAVEdict = {
            "User" : UserName,
            "Password" : Password,
            "RePassword" : RePassword
        }
        if Password == RePassword:
            with open(r"C:\Users\Hp\Desktop\jj\Save.json",mode="w") as file:
                json.dump(SAVEdict, file)
            exit()
        else :
            self.RePassword.setText("")
            self.Password.setText("")
            self.Password.setPlaceholderText("Password And RePassword Aren't Same!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sign_UP = QtWidgets.QDialog()
    ui = Ui_Sign_UP()
    ui.setupUi(Sign_UP)
    Sign_UP.show()
    sys.exit(app.exec())
