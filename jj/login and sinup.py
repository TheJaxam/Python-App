# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import json
import hashlib


User_Loged = None
class Ui_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(342, 357)
        self.Login = QtWidgets.QWidget()
        self.UserName = QtWidgets.QLineEdit(parent=self.Login)
        self.UserName.setGeometry(QtCore.QRect(10, 100, 321, 31))
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLineEdit(parent=self.Login)
        self.Password.setGeometry(QtCore.QRect(10, 180, 321, 31))
        self.Password.setObjectName("Password")
        self.pushButton = QtWidgets.QPushButton(parent=self.Login)
        self.pushButton.setGeometry(QtCore.QRect(90, 270, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Login_B)
        self.Sign_Up = QtWidgets.QPushButton(parent=self.Login)
        self.Sign_Up.setGeometry(QtCore.QRect(60, 270, 100, 51))
        self.Sign_Up.setObjectName("Sign_Up")
        self.Sign_Up.setHidden(True)
        self.Sign_Up.setText("Sign_Up")
        self.label = QtWidgets.QLabel(parent=self.Login)
        self.label.setGeometry(QtCore.QRect(60, 20, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.setCentralWidget(self.Login)
        self.label_2 = QtWidgets.QLabel(parent=self.Login)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:red")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.EROR2 = QtWidgets.QLabel(parent=self.Login)
        self.EROR2.setGeometry(QtCore.QRect(20, 180, 1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EROR2.setFont(font)
        self.EROR2.setStyleSheet("color:red")
        self.EROR2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EROR2.setObjectName("EROR2")
        self.setCentralWidget(self.Login)
        
        self.label_2.setText(("Password Or UserName Is Wrong!"))
        self.EROR2.setText(("Password Or UserName Is Wrong!"))
        self.label_2.setGeometry(QtCore.QRect(20, 100, 301, 31))
        self.EROR2.setGeometry(QtCore.QRect(20, 180, 301, 31))
        self.label_2.setHidden(True)
        self.EROR2.setHidden(True)
        self.w = None
        self.x = None

        self.pushButton.setText("LOGIN")
        self.label.setText("WELLCOME")
    # def retranslateUi(self, Jax):
    #     _translate = QtCore.QCoreApplication.translate
    #     Jax.setWindowTitle(_translate("Jax", "MainWindow"))
        

    def Login_B(self):
        User = self.UserName.text()
        Pass = self.Password.text()
        with open("Save.json", mode="r") as file:
            load = json.load(file)
        Log = False
        for i in load:    
            if User == i["UserN"] and hashlib.sha256(Pass.encode('utf-8')).hexdigest() == i["Password"]:
                global User_Loged
                User_Loged = User
                print("WELLCOME BACK!")
                Log=True
                if self.x is None:
                    self.x = Dashboard()
                self.x.show()
                break
        if Log == False:
            self.UserName.setText("")
            self.Password.setText("")
            self.Sign_Up.setHidden(False)
            self.label_2.setHidden(False)
            self.EROR2.setHidden(False)
            self.pushButton.setGeometry(QtCore.QRect(170, 270, 100, 51))
            self.pushButton.clicked.connect(self.Login_C)
        self.Sign_Up.clicked.connect(self.SignUp)
        self.pushButton.setText("Try Again")
    def Login_C(self): 
        self.label_2.setHidden(True)
        self.EROR2.setHidden(True)
        self.pushButton.setText("Login")
        self.pushButton.clicked.connect(self.Login_B)

    def SignUp(self):
        

        if self.w is None:
            self.w = Ui_Sign_Up()
        self.w.show()

class Ui_Sign_Up(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(342, 357)
        centeralwidget = QtWidgets.QVBoxLayout()
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(100, 270, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Sign_Up)
        self.UserName = QtWidgets.QLineEdit()
        self.UserName.setEnabled(True)
        self.UserName.setGeometry(QtCore.QRect(10, 60, 321, 31))
        self.UserName.setObjectName("UserName")
        self.UserName.setPlaceholderText("Write Your User Name")
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.Password = QtWidgets.QLineEdit()
        self.Password.setEnabled(True)
        self.Password.setGeometry(QtCore.QRect(10, 130, 321, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.Password.setObjectName("Password")
        self.Password.setPlaceholderText("Write Password")
        self.RePassword = QtWidgets.QLineEdit()
        self.RePassword.setEnabled(True)
        self.RePassword.setGeometry(QtCore.QRect(10, 200, 321, 31))
        self.RePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.RePassword.setObjectName("RePassword")
        self.RePassword.setPlaceholderText("Write Password Again")
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton.setText("Sign-Up")
        self.label.setText( "WELLCOME")
        centeralwidget.addWidget(self.label)
        centeralwidget.addWidget(self.UserName)
        centeralwidget.addWidget(self.Password)
        centeralwidget.addWidget(self.RePassword)
        centeralwidget.addWidget(self.pushButton)
        self.setLayout(centeralwidget)

        # self.retranslateUi(Sign_UP)
        # QtCore.QMetaObject.connectSlotsByName(Sign_UP)

    def Sign_Up(self):
        
        UserName = self.UserName.text()
        Password = self.Password.text()
        RePassword = self.RePassword.text()
        

        SAVEdict = {
            "UserN" : UserName,
            "Password" : hashlib.sha256(Password.encode('utf-8')).hexdigest()
        }
        
        with open("Save.json", mode="r") as file:
            load = json.load(file)    
        TUNAME= False
        if UserName != "" and Password != "":
            for i in load:    
                if UserName == i["UserN"]:
                    TUNAME = True
            
            PassRule = False
            PassRL = ["@","#","$"]
            if len(Password) >= 8:
                for i in Password:
                    if i in PassRL:
                        PassRule = True
                        break
                if Password == RePassword and TUNAME == False and PassRule == True:
                    with open("Save.json", mode="r") as file:
                        List = json.load(file)
                        List.append(SAVEdict)
                    file = open("Save.json", mode="w")
                    json.dump(List ,file)
                    self.close()
            
                else :
                    self.UserName.setText("UserName In Already Taket")
                    self.RePassword.setText("")
                    self.Password.setText("")
                    self.Password.setPlaceholderText("Password And RePassword Aren't Same!")
            else:
                print("Password Must Be More Than 8 And @,#,$ Charecters!!")
        else:
            print("Inputs Shouldn't Be Empty!")

class Dashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(342, 357)
        centeralwidget = QtWidgets.QVBoxLayout() 
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.Change_Label()
        self.RPBTN = QtWidgets.QPushButton()
        self.RPBTN.setGeometry(QtCore.QRect(100, 270, 151, 51))
        self.RPBTN.setObjectName("RPBTN")
        self.RPBTN.setText("ResetPassword")
        self.RPBTN.clicked.connect(self.ResetPass)
        self.PLBTN = QtWidgets.QPushButton()
        self.RPBTN.setObjectName("PLBTN")
        self.PLBTN.setObjectName("pushButton")
        self.PLBTN.clicked.connect(self.PassList)
        centeralwidget.addWidget(self.label)
        centeralwidget.addWidget(self.PLBTN)
        centeralwidget.addWidget(self.RPBTN)
        self.setLayout(centeralwidget)
        self.S=None
        self.X= None
    def Change_Label(self):
        global User_Loged
        self.label.setText(f'Wellcome {User_Loged}!!')

    def PassList(self):
        if self.X is None:
            self.X =Password_List()
        self.X.show()

    def ResetPass(self):
        if self.S is None:
            self.S = Reset_Password()
        self.S.show()

class Password_List(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(342, 357)
        centeralwidget = QtWidgets.QVBoxLayout()
        self.Pass_Combo = QtWidgets.QComboBox()
        self.APBTN = QtWidgets.QPushButton()
        self.APBTN.setObjectName("")
        self.APBTN.setText("Add")
        self.APBTN.clicked.connect(self.AddList)
        self.EPBTN = QtWidgets.QPushButton()
        self.EPBTN.setObjectName("Edit")
        self.EPBTN.setText("Edit")
        self.SHPBTN = QtWidgets.QPushButton()
        self.SHPBTN.setObjectName("Show")
        self.SHPBTN.setText("Show")
        self.DPBTN = QtWidgets.QPushButton()
        self.DPBTN.setObjectName("Delet")
        self.DPBTN.setText("Delet")
        self.A = None
        self.E = None
        self.SH = None
        self.D = None

        centeralwidget.addWidget(self.Pass_Combo)
        centeralwidget.addWidget(self.APBTN)
        centeralwidget.addWidget(self.EPBTN)
        centeralwidget.addWidget(self.SHPBTN)
        centeralwidget.addWidget(self.DPBTN)
        self.setLayout(centeralwidget)
                                 
    def AddList(self):
        if self.A is None:
            self.A=Add_Password()
        self.A.show()
            
class Add_Password(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        centeralwidget = QtWidgets.QVBoxLayout()
        self.PassName = QtWidgets.QLineEdit()
        self.PassName.setGeometry(QtCore.QRect(10, 130, 321, 31))
        self.PassName.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.PassName.setObjectName("PassName")
        self.PassName.setPlaceholderText("Write A Name For Your Password!")
        self.PassWord = QtWidgets.QLineEdit()
        self.PassWord.setGeometry(QtCore.QRect(10, 200, 321, 31))
        self.PassWord.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.PassWord.setObjectName("PassWord")
        self.PassWord.setPlaceholderText("Write Your Password!")
        self.Add = QtWidgets.QPushButton()
        self.Add.setText("Add")
        self.Add.clicked.connect(Add_Pass())
        centeralwidget.addWidget(self.PassName)
        centeralwidget.addWidget(self.PassWord)
    # def Add_Pass(self):

class Reset_Password(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(342, 357)
        centeralwidget = QtWidgets.QVBoxLayout()
        self.Old_Password = QtWidgets.QLineEdit()
        self.Old_Password.setEnabled(True)
        self.Old_Password.setGeometry(QtCore.QRect(10, 130, 321, 31))
        self.Old_Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.Old_Password.setObjectName("Old_Password")
        self.Old_Password.setPlaceholderText("Write New Password")
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(100, 270, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Reset_Password)
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.Password = QtWidgets.QLineEdit()
        self.Password.setEnabled(True)
        self.Password.setGeometry(QtCore.QRect(10, 130, 321, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.Password.setObjectName("Password")
        self.Password.setPlaceholderText("Write New Password")
        self.RePassword = QtWidgets.QLineEdit()
        self.RePassword.setEnabled(True)
        self.RePassword.setGeometry(QtCore.QRect(10, 200, 321, 31))
        self.RePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.RePassword.setObjectName("RePassword")
        self.RePassword.setPlaceholderText("Write New Password Again")
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton.setText("Sign-Up")
        centeralwidget.addWidget(self.label)
        centeralwidget.addWidget(self.Old_Password)
        centeralwidget.addWidget(self.Password)
        centeralwidget.addWidget(self.RePassword)
        centeralwidget.addWidget(self.pushButton)
        self.setLayout(centeralwidget)
    
    def Change_Label(self):
        global User_Loged
        self.label.setText(f'Wellcome {User_Loged}!!')

    def Reset_Password(self):
        Old_Pass = self.Old_Password.text()
        NPass = self.Password.text()
        NRePass = self.RePassword.text()
        PassRule = False
        PassRL = ["@","#","$"]
        if len(Old_Pass) >= 8 and len(NPass) >= 8 and len(NRePass) >= 8:
            for i in NPass:
                if i in PassRL:
                    PassRule = True
                    break
        if Old_Pass != "" and NPass != "" :
                if NPass == NRePass :
                    if PassRule == True:
                        with open("Save.json", mode="r") as file:
                            load = json.load(file)
                        for i in load:
                            if hashlib.sha256(Old_Pass.encode('utf-8')).hexdigest() == i["Password"] and User_Loged == i["UserN"]:
                                i["Password"] = hashlib.sha256(NPass.encode('utf-8')).hexdigest()

                                file = open("Save.json", mode="w")
                                json.dump(load ,file)
                                self.close()
                    else:
                        print("Password Must Be More Than 8 And @,#,$ Charecters!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_login()
    ui.show()
    
    sys.exit(app.exec())
