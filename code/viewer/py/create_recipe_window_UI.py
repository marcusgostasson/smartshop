from pathlib import Path

import login_window
import smartshop_mysql
import start_window
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class CreateRecipeWindow(QWidget):
    """class for the create recipe window."""

    def __init__(self):
        self.at_least_one_ingredient_picked = False

    def set_up_create_recipe_window(self, user_name):
        """Set up the window."""
        self.user_name = user_name
        self.login_window = login_window.LoginWindow()
        self.start_window = start_window.UIMainWindow(user_name)
        self.db_instance = smartshop_mysql.SmartShopDB()

        super().__init__()
        # Get the path to the viewer folder
        viewer_path = Path(__file__).resolve().parent.parent
        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI" / "create_recipe_window.ui"
        loadUi(ui_file_path, self)

        self.box = self.findChild(QWidget, "scrollAreaWidgetContents")

        scroll_area_layout = QVBoxLayout()
        self.box.setLayout(scroll_area_layout)

        self.recipe_name = self.findChild(QLineEdit, "recept_name")

        self.recipe_steps = self.findChild(QTextEdit, "recepie_steps")

        self.user_product_choice = self.findChild(QLineEdit, "type_in_recipe")
        self.ingrediense_box = self.findChild(QComboBox, "ingrediense_box")
        self.search_ingrediense = self.findChild(
            QPushButton, "search_ingredient_button"
        )
        self.search_ingrediense.clicked.connect(self.handle_search)

        self.back_to_start_wind = self.findChild(QPushButton, "back_to_start_wind")
        self.back_to_start_wind.clicked.connect(self.back_to_start_window)

        self.add_ingredient_button = self.findChild(
            QPushButton, "add_ingrediense_button"
        )
        self.add_ingredient_button.clicked.connect(
            lambda: self.add_ingredient(self.ingrediense_box.currentText())
        )
        self.ingrediense_list_id = []
        self.picked_ingrediens = []

        self.create_recipe_button = self.findChild(QPushButton, "create_recipe_button")
        self.create_recipe_button.clicked.connect(
            lambda: self.create_recipe(self.user_name)
        )

        self.show()

    def back_to_start_window(self):
        """back to start window"""
        self.hide()
        self.start_window.set_up_start_menu()

    def create_recipe(self, user_name):
        """Create a recipe."""
        if not self.at_least_one_ingredient_picked:
            self.login_window.error_message("Måste ha minst en ingrediens")
            # self.set_up_create_recipe_window(user_name)
        elif self.at_least_one_ingredient_picked:
            does_recipe_exist = self.db_instance.get_recipe_name(
                self.recipe_name.text()
            )
            if does_recipe_exist:
                self.login_window.error_message(
                    "Namnet på ditt recept finns redan, välj ett annat"
                )
            elif self.recipe_name.text() == "":
                self.login_window.error_message("Du behöver namnge ditt recept")
            else:
                self.db_instance.insert_user_recipe(
                    self.recipe_name.text(),
                    user_name,
                    self.recipe_steps.toPlainText(),
                    self.ingrediense_list_id,
                )
                self.hide()
                self.start_window.set_up_start_menu()

    def add_ingredient(self, ingrediense):
        """add ingredient to the list of ingredients for the recipe."""
        self.at_least_one_ingredient_picked = True
        if ingrediense != "":
            just_product_name = ingrediense.split(" ")[0]
            if ingrediense not in self.picked_ingrediens:
                product_id = self.db_instance.get_product_id(just_product_name)
                self.ingrediense_list_id.append(product_id)
                self.picked_ingrediens.append(ingrediense)
                ingredient = QLabel(ingrediense)
                ingredient.setStyleSheet(
                    "font: 14px 'Arial Black'; font-weight: bold; background-color: rgb(255, 255, 255);"
                )
                ingredient.setFixedSize(237, 50)
                ingredient.setAlignment(Qt.AlignCenter)
                self.box.layout().insertWidget(0, ingredient)
            else:
                self.login_window.error_message(
                    "Har redan " + ingrediense + " i ditt recept"
                )

    def handle_search(self):
        """Handle search for ingredients."""
        product_name = self.user_product_choice.text()
        ingredients = self.db_instance.get_ingrediense(product_name)
        self.ingrediense_box.clear()
        self.ingrediense_box.addItems(ingredients)
