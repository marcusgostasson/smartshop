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
        """Testing if the windows name is correct."""
        self.app = QApplication(sys.argv)
        self.window = window_for_stores_and_ingredients_price.IngredientPrice()
        self.window.set_up_ingredient_price_window(MagicMock(), MagicMock(), "sven")
        self.assertEqual(self.window.windowTitle(), "Ingredienser för receptet")

    def test_click_return_to_start_window_button(self):
        """Testing if 'Tillbaka till meny' is working."""
        self.app = QApplication(sys.argv)
        self.window = window_for_stores_and_ingredients_price.IngredientPrice()
        self.window.set_up_ingredient_price_window(MagicMock(), MagicMock(), "sven")

        button = self.window.return_to_start_window_button
        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.window.start_menu_window.set_up_start_menu.called)

    def test_click_steps_for_recipe_button(self):
        """Testing if 'Stegen till receptet' button works."""
        self.app = QApplication(sys.argv)
        self.window = window_for_stores_and_ingredients_price.IngredientPrice()
        self.window.set_up_ingredient_price_window(MagicMock(), MagicMock(), "sven")

        button = self.window.get_steps_for_recipe_button
        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(
            self.window.steps_for_chosen_recipe.set_up_recipe_step_window.called
        )


if __name__ == "__main__":
    unittest.main()
