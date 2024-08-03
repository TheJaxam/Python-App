from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 399)
        self.Save = QtWidgets.QPushButton(parent=Dialog)
        self.Save.setGeometry(QtCore.QRect(244, 360, 81, 31))
        self.Save.setObjectName("Save")
        self.Save.clicked.connect(self.Submiit)
        self.cancel = QtWidgets.QPushButton(parent=Dialog)
        self.cancel.setGeometry(QtCore.QRect(40, 360, 81, 31))
        self.cancel.setObjectName("cancel")
        self.Name = QtWidgets.QLineEdit(parent=Dialog)
        self.Name.setGeometry(QtCore.QRect(10, 20, 339, 22))
        self.Name.setAccessibleDescription("")
        self.Name.setObjectName("Name")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 80, 339, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Gender = QtWidgets.QComboBox(parent=Dialog)
        self.Gender.setEnabled(True)
        self.Gender.setGeometry(QtCore.QRect(10, 140, 339, 22))
        self.Gender.setMaximumSize(QtCore.QSize(16777215, 22))
        self.Gender.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Gender.setMouseTracking(False)
        self.Gender.setObjectName("Gender")
        self.Gender.addItem("")
        self.Gender.setItemText(0, "Select One")
        self.Gender.addItem("")
        self.Gender.addItem("")
        self.Code = QtWidgets.QLineEdit(parent=Dialog)
        self.Code.setGeometry(QtCore.QRect(10, 230, 339, 22))
        self.Code.setObjectName("Code")
        self.Birth = QtWidgets.QDateEdit(parent=Dialog)
        self.Birth.setGeometry(QtCore.QRect(10, 190, 341, 22))
        self.Birth.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.Birth.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2024, 12, 31), QtCore.QTime(20, 29, 59)))
        self.Birth.setObjectName("Birth")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Save.setText(_translate("Dialog", "Save"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.Name.setText(_translate("Dialog", "Name:"))
        self.lineEdit_3.setText(_translate("Dialog", "Family:"))
        self.Gender.setItemText(1, _translate("Dialog", "Male"))
        self.Gender.setItemText(2, _translate("Dialog", "Female"))
        self.Code.setText(_translate("Dialog", "Nathional Code:"))

    def Submiit(self):
        Name = self.Name.text()
        try:
            Code = int(self.Code.text())
        except:
            Code = str(self.Code.text())
            print (Code + "Is Not Number")
        Gender = str(self.Gender.currentText)
        Birth = self.Birth.date()
        Family = self.lineEdit_3.text()
        print(Name,Code,Family,Gender,Birth)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
