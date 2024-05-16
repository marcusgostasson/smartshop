import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication

sys.modules["smartshop_mysql"] = MagicMock()
sys.modules["window_for_stores_and_ingredients_price"] = MagicMock()
sys.modules["create_user_window"] = MagicMock()
sys.modules["start_window"] = MagicMock()

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.py import login_window


class TestLoginWindow(unittest.TestCase):
    """Testing the login window."""

    def test_window_title_login(self):
        """Testing if the name of the window is correct."""
        self.app = QApplication(sys.argv)
        self.window = login_window.LoginWindow()
        self.window.set_up_login()
        self.assertEqual(self.window.windowTitle(), "Logga in")


if __name__ == "__main__":
    unittest.main()
