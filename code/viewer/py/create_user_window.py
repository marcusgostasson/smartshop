"""Class for create_user_window."""
import login_window
import smartshop_mysql
import re
#from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QDesktopWidget, QGridLayout, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from passlib.hash import bcrypt
from pathlib import Path


class CreateUserWindow(QWidget):
    """Create create_user_window class."""

    def __init__(self):
        """Initialize the object."""
        super().__init__()

        # Window
        viewer_path = Path(__file__).resolve().parent.parent

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI/create_user.ui"

        loadUi(f"{ui_file_path}", self)
        self.setWindowTitle("Skapa användare")
        grid = QGridLayout()
        self.setLayout(grid)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Instanses

        self.db_instance = smartshop_mysql.SmartShopDB()

        # Text

        self.first_name = self.findChild(QLineEdit, "first_name")
        self.last_name = self.findChild(QLineEdit, "last_name")
        self.username_create = self.findChild(QLineEdit, "username")
        self.email = self.findChild(QLineEdit, "email")
        self.password_user = self.findChild(QLineEdit, "password_user")
        self.password_user.setEchoMode(QLineEdit.Password)
        self.confirm_password = self.findChild(QLineEdit, "confirm_password")
        self.confirm_password.setEchoMode(QLineEdit.Password)

        # Bottons

        self.create = self.findChild(QPushButton, "create")
        self.create.clicked.connect(self.create_account)

    def create_account(self):
        """Create account."""
        first_name = self.first_name.text().strip().title()
        last_name = self.last_name.text().strip().title()
        username_create = self.username_create.text().strip()
        email = self.email.text().strip()
        password_user = self.password_user.text().strip()
        confirm_password = self.confirm_password.text().strip()

        if not (first_name and last_name and username_create and email and
                password_user and confirm_password):
            self.error_message("Alla fält måste vara ifyllda.")
            return

        if not self.validate_email(email):
            self.error_message("Formatet på E-mail är fel.")
            return

        if self.db_instance.get_username_data_base(username_create):
            self.error_message("Användarnamn finns redan")
            return

        if password_user != confirm_password:
            self.error_message("Lösenorden stämmer inte överens, försök igen!")
            return

        hashed_pass = bcrypt.hash(password_user)
        self.db_instance.create_user(first_name, last_name, username_create,
                                     email, hashed_pass)

        self.hide()
        self.login = login_window.LoginWindow()

    def validate_email(self, email):
        """Check if the email is set correctly."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def error_message(self, message):
        """Error messages."""
        self.message_box = QMessageBox()
        self.message_box.setWindowTitle('Error')
        self.message_box.setText(f'{message}')
        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.exec_()
