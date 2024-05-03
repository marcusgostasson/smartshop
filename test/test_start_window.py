import unittest
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from unittest.mock import MagicMock

sys.modules['smartshop_mysql'] = MagicMock()
sys.modules['window_for_stores_and_ingredients_price'] = MagicMock()

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.viewer.py import start_window

class TestApp(unittest.TestCase):
    def test_window_title(self):
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        self.assertEqual(self.window.windowTitle(), "SmartShop")

    def test_button(self):
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        button = self.window.get_ingredients_button

        self.window.second_window.set_up_ingredient_price_window = MagicMock()

        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.window.second_window.set_up_ingredient_price_window.called)


if __name__ == '__main__':
    unittest.main()