import unittest
import sys
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from unittest.mock import MagicMock

sys.modules['smartshop_mysql'] = MagicMock()
sys.modules['window_for_stores_and_ingredients_price'] = MagicMock()

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.viewer.py import start_window

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow()


    def test_app_title(self):
        self.assertEqual(self.app.windowTitle(), "SmartShop")


if __name__ == '__main__':
    unittest.main()
