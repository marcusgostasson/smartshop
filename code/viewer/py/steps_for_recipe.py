from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from pathlib import Path
import window_for_stores_and_ingredients_price


class RecipeSteps(QWidget):
    """Recipe steps class."""

    def set_up_recipe_step_window(
        self, db_instance, recipe, start_menu_window, user_name
    ):
        """Set up the window."""
        self.user_name = user_name
        self.start_menu_window = start_menu_window
        self.previous_window = window_for_stores_and_ingredients_price.IngredientPrice()
        super().__init__()
        viewer_path = Path(__file__).resolve().parent.parent

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI" / "recept_step_window.ui"

        # Load the UI file
        loadUi(ui_file_path, self)

        self.recipe = recipe

        vertical_layout = QVBoxLayout()

        self.recipe_name = self.findChild(QLabel, "recept_name")
        self.recipe_steps = self.findChild(QLabel, "recept_steps")

        self.recipe_picture = self.findChild(QLabel, "recept_picture")
        viewer_path = Path(__file__).resolve().parent.parent
        ui_file_path_for_picture = viewer_path / "pictures"
        recipe_image = QPixmap(f"{ui_file_path_for_picture}/{recipe}.png")
        recipe_image = recipe_image.scaled(400, 400)
        self.recipe_picture.setPixmap(recipe_image)
        vertical_layout.addWidget(self.recipe_picture)

        self.db_instance = db_instance
        recipe_step = self.db_instance.get_steps_for_recipe(recipe)
        if recipe_step is None:
            self.recipe_name.setText(recipe)
            vertical_layout.addWidget(self.recipe_name)
            self.recipe_name.adjustSize()

            self.recipe_steps.setText("Inga steg till detta recept")
            vertical_layout.addWidget(self.recipe_steps)
            self.recipe_steps.adjustSize()
        else:
            self.recipe_name.setText(recipe)
            vertical_layout.addWidget(self.recipe_name)
            self.recipe_name.adjustSize()

            self.recipe_steps.setText(recipe_step)
            vertical_layout.addWidget(self.recipe_steps)
            self.recipe_steps.adjustSize()

        self.return_button = QPushButton("Tillbaka")
        style = self.set_button_style()
        self.return_button.setStyleSheet(style)
        vertical_layout.addWidget(self.return_button)
        self.return_button.clicked.connect(self.return_to_previous_window)

        self.setLayout(vertical_layout)

        self.show()

    def return_to_previous_window(self):
        """Hide current window and opens IngredientPrice class."""
        self.hide()
        self.previous_window.set_up_ingredient_price_window(
            self.start_menu_window, self.recipe, self.user_name
        )

    def set_button_style(self):
        """Set the style for the button."""
        button_style = """QPushButton {\n	
        border-style: solid;\n	
        border-color: #9999aa;\n	
        border-radius: 5px;\n	
        color: white;\n	
        background-color: #3474eb;
        font-family: Arial Black;
        font-size: 16px;
        Height: 50px
        \n}\n
        \nQPushButton:enabled {\n	
        background-color: #2C65A4;\n	
        color: white;\n}\n
        \nQPushButton:pressed {\n	
        background-color: #0d2f72;\n	
        color: #fffffe;\n}\n
        \nQPushButton:hover:!pressed {\n	
        background-color: #0034AB;\n	
        color: white;\n}\n
        \nQPushButton:disabled {\n	
        background-color: #aaaaaa;\n	
        color: #ffffff;\n}
        """
        return button_style
