import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton


sys.modules["smartshop_mysql"] = MagicMock()
sys.modules["window_for_stores_and_ingredients_price"] = MagicMock()

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.py import steps_for_recipe


class TestStepsForRecipe(unittest.TestCase):
    def test_click_return_to_previous_window(self):
        """Testing if return to previous window works."""
        self.app = QApplication(sys.argv)

        self.window = steps_for_recipe.RecipeSteps()
        db_instance = MagicMock()
        db_instance.get_steps_for_recipe.return_value = "Step 1: Prepare ingredients"

        self.window.set_up_recipe_step_window(db_instance, "tacos", MagicMock(), "sven")

        QTest.mouseClick(self.window.return_button, Qt.LeftButton)

        self.assertTrue(
            self.window.previous_window.set_up_ingredient_price_window.called
        )

    def test_widgets_exist(self):
        """Testing if the labels are able to be found."""
        self.app = QApplication(sys.argv)

        self.window = steps_for_recipe.RecipeSteps()
        db_instance = MagicMock()
        db_instance.get_steps_for_recipe.return_value = "Step 1: Prepare ingredients"
        self.window.set_up_recipe_step_window(db_instance, "tacos", MagicMock(), "sven")

        recipe_name = self.window.findChild(QLabel, "recept_name")
        recipe_steps = self.window.findChild(QLabel, "recept_steps")
        recipe_picture = self.window.findChild(QLabel, "recept_picture")

        self.assertIsNotNone(recipe_name)
        self.assertIsNotNone(recipe_steps)
        self.assertIsNotNone(recipe_picture)


if __name__ == "__main__":
    unittest.main()
