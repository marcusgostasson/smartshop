import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QPushButton

sys.modules["smartshop_mysql"] = MagicMock()
sys.modules["login_window"] = MagicMock()


script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.py import create_user_window


class TestCreateUserWindow(unittest.TestCase):
    def test_window_title(self):
        """Testing if the name of the window is correct."""
        app = QApplication(sys.argv)
        window = create_user_window.CreateUserWindow()
        window.set_up_window()
        self.assertEqual(window.windowTitle(), "Skapa användare")

    def test_validate_email(self):
        """Testing if valid email is returning True for correct email format
        and False for incorrect format."""
        app = QApplication(sys.argv)
        window = create_user_window.CreateUserWindow()
        exp = True
        res = window.validate_email("raz@hotmail.com")
        self.assertEqual(exp, res)

        exp = False
        res = window.validate_email("razhotmail.com")
        self.assertEqual(exp, res)

    def test_back_button_exist(self):
        """Testing that the back button exist."""
        app = QApplication(sys.argv)
        window = create_user_window.CreateUserWindow()
        window.set_up_window()
        back_button = window.findChild(QPushButton, "back")

        self.assertIsNotNone(back_button)


if __name__ == "__main__":
    unittest.main()
