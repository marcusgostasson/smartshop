import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

sys.modules["smartshop_mysql"] = MagicMock()
sys.modules["window_for_stores_and_ingredients_price"] = MagicMock()
sys.modules["create_recipe_window_UI"] = MagicMock()
sys.modules["login_window"] = MagicMock()


script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.viewer.py import start_window


class TestApp(unittest.TestCase):
    def test_window_title(self):
        """Testing if the name of the window is correct."""
        self.app = QApplication(sys.argv)
        user_name = "raz"
        self.window = start_window.UIMainWindow(user_name)
        self.window.set_up_start_menu()
        self.assertEqual(self.window.windowTitle(), "SmartShop")

    def test_button(self):
        """Testing if pressing 'Hämta ingredienser' is opening other window."""
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        self.window.set_up_start_menu()
        button = self.window.get_ingredients_button

        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.window.second_window.set_up_ingredient_price_window.called)


if __name__ == "__main__":
    unittest.main()
