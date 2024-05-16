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

from smartshop.code.py import start_window


class TestStartWindow(unittest.TestCase):
    def test_window_title(self):
        """Testing if the name of the window is correct."""
        app = QApplication(sys.argv)
        user_name = "raz"
        window = start_window.UIMainWindow(user_name)
        window.set_up_start_menu()
        self.assertEqual(window.windowTitle(), "SmartShop")

    def test_button_click_get_ingredients(self):
        """Testing if pressing 'Hämta ingredienser' is opening other window."""
        app = QApplication(sys.argv)
        window = start_window.UIMainWindow("raz")
        window.set_up_start_menu()
        button = window.get_ingredients_button

        QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(window.second_window.set_up_ingredient_price_window.called)

    def test_button_click_user_get_ingredients(self):
        """Testing if pressing users 'Hämta ingredienser' is opening other window."""
        app = QApplication(sys.argv)
        window = start_window.UIMainWindow("raz")
        window.set_up_start_menu()
        button = window.user_get_ingredients_button

        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(window.second_window.set_up_ingredient_price_window.called)

    def test_click_create_recipe_button(self):
        """Testing the 'Skapa recept' button works."""
        app = QApplication(sys.argv)
        window = start_window.UIMainWindow("raz")
        window.set_up_start_menu()
        button = window.create_recipe_button

        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(
            window.create_recipe_instance.set_up_create_recipe_window.called
        )

    def test_click_delete_recipe_button(self):
        """Testing the 'Radera recept' button."""
        app = QApplication(sys.argv)
        window = start_window.UIMainWindow("raz")
        window.set_up_start_menu()
        window.user_ingredients_for_recipe = MagicMock()
        button = window.delete_recipe_button
        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(window.db_instance.delete_recipe.called)

    def test_click_logout_button(self):
        """Testing if the user can logout."""
        app = QApplication(sys.argv)
        window = start_window.UIMainWindow("raz")
        window.set_up_start_menu()
        button = window.logout_button
        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(window.login_window.set_up_login.called)


if __name__ == "__main__":
    unittest.main()
