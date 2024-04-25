"""Class for create_user_window."""
import login_window
import smartshop_mysql
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.uic import loadUi
from passlib.hash import bcrypt


class CreateUserWindow(QWidget):
    """Constructor for CreateUserWindow."""
    def __init__(self):
        super().__init__()
        loadUi("code/viewer/UI/create_user.ui", self)
        self.setWindowTitle("Skapa användare")
        self.db_instance = smartshop_mysql.SMARTSHOP_DB()

        # Text
        self.first_name = self.findChild(QLineEdit, "first_name")
        self.last_name = self.findChild(QLineEdit, "last_name")
        self.username_create = self.findChild(QLineEdit, "username")
        self.email = self.findChild(QLineEdit, "email")
        self.password_user = self.findChild(QLineEdit, "password_user")
        self.confirm_password = self.findChild(QLineEdit, "confirm_password")

        # Button

        self.create = self.findChild(QPushButton, "create")
        self.create.clicked.connect(self.create_account)

    def create_account(self):
        """Take the parameters for create account."""
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        username_create = self.username_create.text()
        email = self.email.text()
        password_user = self.password_user.text()
        confirm_password = self.confirm_password.text()

        self.check_password(first_name, last_name, username_create,
                            email, password_user, confirm_password)

    def check_password(self, first_name, last_name, username_create,
                       email, password_user, confirm_password):
        """Check password."""

        if password_user == confirm_password:
            hashed_password = bcrypt.hash(password_user)
            self.db_instance.create_user(first_name, last_name,
                                         username_create, email,
                                         hashed_password)
            self.hide()
            self.login = login_window.LoginWindow()

        else:
            print("Lösenorden matchade inte försök igen")
