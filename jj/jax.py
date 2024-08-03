import sys
from PySide6.QtWidgets import  QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout

class AppDemo(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Input Example With QLineEdit") 
        self.setGeometry(100, 100, 500, 500)        

        # self.layout1 = QHBoxLayout()        
        # self.layout = QVBoxLayout()        
        self.layout2 = QHBoxLayout()
        

        self.qline1 = QLineEdit()
        self.layout2.addWidget(self.qline1)
        
        self.button = QPushButton("+++++++++++++", self)
        self.layout2.addWidget(self.button)
        
        self.button3 = QPushButton("-", self)
        self.layout2.addWidget(self.button3)


        self.qline2 = QLineEdit()
        self.layout2.addWidget(self.qline2)
        self.setLayout(s0)


app=QApplication(sys.argv)
demo=AppDemo()
demo.show()
sys.exit(app.exec_())