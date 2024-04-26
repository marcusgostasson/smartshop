from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from pathlib import Path
import window_for_stores_and_ingredients_price


class Recipe_steps(QWidget):
    def __init__(self):
        pass

    def set_up_recipe_step_window(self, db_instance, recipe, start_menu_window):
        self.start_menu_window = start_menu_window
        self.previous_window = window_for_stores_and_ingredients_price.ingredient_price()
        super().__init__()
        viewer_path = Path(__file__).resolve().parent.parent / "viewer"

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI" / "recept_step_window.ui"

        # Load the UI file
        loadUi(ui_file_path, self)
        self.recipe = recipe
        
        vertical_layout = QVBoxLayout()
        
        self.recipe_name = self.findChild(QLabel, "recept_name")
        self.recipe_steps = self.findChild(QLabel, "recept_steps")

        self.db_instance = db_instance
        recipe_step = self.db_instance.get_steps_for_recipe(recipe)
        if recipe_step is None:
            self.recipe_name.setText(recipe)
            vertical_layout.addWidget(self.recipe_name)
            self.recipe_name.adjustSize()

            self.recipe_steps.setText("No steps for this recipe")
            vertical_layout.addWidget(self.recipe_steps)
            self.recipe_steps.adjustSize()
        else:
            self.recipe_name.setText("Stegen till " + recipe)
            vertical_layout.addWidget(self.recipe_name)
            self.recipe_name.adjustSize()

            self.recipe_steps.setText(recipe_step)
            vertical_layout.addWidget(self.recipe_steps)
            self.recipe_steps.adjustSize()

        self.return_button = QPushButton("Tillbaka")
        vertical_layout.addWidget(self.return_button)
        self.return_button.clicked.connect(self.return_to_previous_window)
        
        self.setLayout(vertical_layout)
        
        self.show()

    def return_to_previous_window(self):
        self.hide()
        self.previous_window.set_up_ingredient_price_window(self.start_menu_window, self.recipe)