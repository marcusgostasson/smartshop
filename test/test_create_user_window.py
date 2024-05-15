import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

sys.modules["smartshop_mysql"] = MagicMock()
sys.modules["login_window"] = MagicMock()


script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.py import create_user_window


class TestCreateUserWindow(unittest.TestCase):
    def test_window_title(self):
        """Testing if the name of the window is correct."""
        self.app = QApplication(sys.argv)
        self.window = create_user_window.CreateUserWindow()
        self.window.set_up_window()
        self.assertEqual(self.window.windowTitle(), "Skapa användare")


if __name__ == "__main__":
    unittest.main()
