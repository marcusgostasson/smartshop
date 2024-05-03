"""Class for login_window."""
import sys
import create_user_window
import start_window
import smartshop_mysql
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from passlib.hash import bcrypt
from pathlib import Path


class LoginWindow(QMainWindow):
    """Login window class for user authentication."""

    def __init__(self):
        """Initialize the object."""
        super().__init__()

        # Instans
    
        self.database = smartshop_mysql.SmartShopDB()

        # Screen

        viewer_path = Path(__file__).resolve().parent.parent
        ui_file_path = viewer_path / "UI/login.ui"
        loadUi(f"{ui_file_path}", self)
        self.setWindowTitle("Logga in")
        viewer_path = Path(__file__).resolve().parent.parent
        self.setWindowIcon(QIcon(f'{viewer_path}/pictures/smartshoplogo.png'))

        # Logo

        self.logo_picture = self.findChild(QLabel, "logo")
        logo_pixmap = QPixmap(f'{viewer_path}/pictures/smartshoplogo1.png')
        self.logo_picture.setPixmap(logo_pixmap)

        # Center window

        grid = QGridLayout()
        self.setLayout(grid)
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

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
        """Take the parameter in and check."""
        username = self.username.text()
        password = self.password.text()
        self.check_login(username, password)

    def check_login(self, username, input_password):
        """Validate credentials against stored data."""
        try:
            stored_hash = self.database.get_password_hash(username)
            if stored_hash and self.compare_password(input_password,
                                                     stored_hash):
                self.hide()
                self.start_window = start_window.UIMainWindow(username)
                self.start_window.show()
            else:
                self.error_message("""Användarnamn eller lösenord är felaktigt,
försök igen!""")
        except Exception as e:
            self.error_message(f"Login error: {str(e)}")

    def hash_password(self, password):
        """Hash the password using bcrypt."""
        return bcrypt.hash(password)

    def compare_password(self, input_password, stored_hash):
        """Compare input password against the stored hash."""
        try:
            return bcrypt.verify(input_password, stored_hash)
        except Exception as e:
            self.error_message(f"Password comparison error: {str(e)}")
        return False

    def create_account_user(self):
        """Switch to account creation window."""
        self.hide()
        self.create_user_window = create_user_window.CreateUserWindow()
        self.create_user_window.show()

    def error_message(self, message):
        """Error messages."""
        self.message_box = QMessageBox()
        self.message_box.setWindowTitle('Error')
        self.message_box.setText(f'{message}')
        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    sys.exit(app.exec_())
