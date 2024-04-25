"""Class for login_window."""
import sys
import create_user_window
import smartshop_mysql
import start_window
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.uic import loadUi
from passlib.hash import bcrypt


class LoginWindow(QMainWindow):
    """Constructor for LoginWindow."""
    def __init__(self):
        super().__init__()
        loadUi("code/viewer/UI/login.ui", self)
        self.setWindowTitle("Logga in")

        # Text
        self.username = self.findChild(QLineEdit, "username_line_edit")
        self.password = self.findChild(QLineEdit, "password_line_edit")
        self.password.setEchoMode(QLineEdit.Password)

        # Buttons
        self.login = self.findChild(QPushButton, "login_button")
        self.login.clicked.connect(self.login_user)

        self.create_account = self.findChild(QPushButton,
                                             "create_account_button")
        self.create_account.clicked.connect(self.create_account_user)
        self.show()

    def login_user(self):
        """Take the parameters username and password."""
        username = self.username.text()
        password = self.password.text()
        hashed_password = bcrypt.hash(password)
        self.check_login(username, hashed_password)

    def check_login(self, username, hashed_password):
        """Check if username and password exist in database"""
        self.check_login_database = smartshop_mysql.SMARTSHOP_DB()
        username_and_password = self.check_login_database.get_username_and_password(username, hashed_password)
        for fetched_user_name_and_password in username_and_password:
            for user_name, password in fetched_user_name_and_password:
                if user_name == username and password == hashed_password:
                    self.hide()
                    self.controlled = start_window.UI_main_window()
                else:
                    print("Användarnamn eller lösenord är fel prova igen")

    def create_account_user(self):
        """Close login_window and start create_user window and show
           create_user window"""
        self.hide()
        self.create_user_window = create_user_window.CreateUserWindow()
        self.create_user_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    sys.exit(app.exec_())
