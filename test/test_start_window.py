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

    def test_button_click_get_ingredients(self):
        """Testing if pressing 'Hämta ingredienser' is opening other window."""
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        self.window.set_up_start_menu()
        button = self.window.get_ingredients_button

        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.window.second_window.set_up_ingredient_price_window.called)

    def test_button_click_user_get_ingredients(self):
        """Testing if pressing users 'Hämta ingredienser' is opening other window."""
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        self.window.set_up_start_menu()
        button = self.window.user_get_ingredients_button

        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(self.window.second_window.set_up_ingredient_price_window.called)

    def test_click_create_recipe_button(self):
        """Testing the 'Skapa recept' button works."""
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        self.window.set_up_start_menu()
        button = self.window.create_recipe_button

        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(
            self.window.create_recipe_instance.set_up_create_recipe_window.called
        )

    def test_click_delete_recipe_button(self):
        """Testing the 'Radera recept' button."""
        self.app = QApplication(sys.argv)
        self.window = start_window.UIMainWindow("raz")
        self.window.set_up_start_menu()
        self.window.user_ingredients_for_recipe = MagicMock()
        button = self.window.delete_recipe_button
        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(self.window.db_instance.delete_recipe.called)


if __name__ == "__main__":
    unittest.main()
