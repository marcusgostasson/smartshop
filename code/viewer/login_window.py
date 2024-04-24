from passlib.hash import bcrypt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import sys

class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("code/viewer/UI/login.ui", self)
        self.setWindowTitle("Logga in")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.createcustomer)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.show()

    def krypt_password(self, password):
        """Krypterar lösenordet."""
        try:
            hash_password = bcrypt.hash(password)
            print(hash_password)
        except Exception as e:
            print("Ett fel uppstod vid kryptering av lösenord:", e)

    def login(self):
        """"Tar in användarnamn och lösenord."""
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(username)
        print(password)
        self.krypt_password(password)

    def createcustomer(self):
        pass

app = QApplication(sys.argv)
login_window1 = login_window()
app.exec_()
