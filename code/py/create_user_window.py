"""Class for create_user_window."""

import re
from pathlib import Path

import login_window
import smartshop_mysql
from passlib.hash import bcrypt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class CreateUserWindow(QWidget):
    """Create create_user_window class."""

    def __init__(self):
        self.login_window_instance = login_window.LoginWindow()
        self.db_instance = smartshop_mysql.SmartShopDB()

    def set_up_window(self):
        """Initialize the object."""
        super().__init__()

        # Window
        viewer_path = Path(__file__).resolve().parent.parent

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI/create_user.ui"

        loadUi(f"{ui_file_path}", self)
        self.setWindowTitle("Skapa användare")
        grid = QGridLayout()

        # Logo

        self.logo_picture = self.findChild(QLabel, "logo")
        logo_pixmap = QPixmap(f"{viewer_path}/pictures/smartshoplogo.png")
        self.logo_picture.setPixmap(logo_pixmap)

        # Center window

        self.setLayout(grid)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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

        self.back = self.findChild(QPushButton, "back")
        self.back.clicked.connect(self.back_to_login)

    def back_to_login(self):
        """Go back to login window."""
        self.hide()
        self.login_window_instance.set_up_login()

    def create_account(self):
        """Create useraccount."""
        first_name = self.first_name.text().strip().title()
        last_name = self.last_name.text().strip().title()
        username_create = self.username_create.text().strip()
        email = self.email.text().strip()
        password_user = self.password_user.text().strip()
        confirm_password = self.confirm_password.text().strip()

        if not (
            first_name
            and last_name
            and username_create
            and email
            and password_user
            and confirm_password
        ):
            self.login_window_instance.error_message("Alla fält måste vara ifyllda.")
            return

        if not self.validate_email(email):
            self.login_window_instance.error_message("Formatet på E-mail är fel.")
            return

        if self.db_instance.get_username_data_base(username_create):
            self.login_window_instance.error_message("Användarnamn finns redan")
            return

        if password_user != confirm_password:
            self.login_window_instance.error_message(
                "Lösenorden stämmer inte överens, försök igen!"
            )
            return

        hashed_pass = bcrypt.hash(password_user)
        self.db_instance.create_user(
            first_name, last_name, username_create, email, hashed_pass
        )

        self.hide()
        # self.login = login_window.LoginWindow()
        self.login_window_instance.set_up_login()

    def validate_email(self, email):
        """Check if the email is set correctly."""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return True
        else:
            return False
