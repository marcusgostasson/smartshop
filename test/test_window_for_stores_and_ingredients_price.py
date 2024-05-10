import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

sys.modules["smartshop_mysql"] = MagicMock()
sys.modules["start_window"] = MagicMock()
sys.modules["steps_for_recipe"] = MagicMock()
sys.modules["login_window"] = MagicMock()


script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.viewer.py import window_for_stores_and_ingredients_price


class TestIngredientPrice(unittest.TestCase):
    def test_window_title(self):
        self.app = QApplication(sys.argv)
        self.window = window_for_stores_and_ingredients_price.IngredientPrice()
        self.window.set_up_ingredient_price_window(MagicMock(), MagicMock(), "sven")
        self.assertEqual(self.window.windowTitle(), "Ingredienser för receptet")

    def test_button(self):
        self.app = QApplication(sys.argv)
        self.window = window_for_stores_and_ingredients_price.IngredientPrice()
        self.window.set_up_ingredient_price_window(MagicMock(), MagicMock(), "sven")
        layout = self.window.layout()
        button = layout.itemAt(0).widget()

        self.window.start_menu_window.set_up_start_menu = MagicMock()

        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.window.start_menu_window.set_up_start_menu.called)


if __name__ == "__main__":
    unittest.main()
