"""Class for the start window."""

from pathlib import Path
import create_recipe_window_UI
import login_window
import smartshop_mysql
import window_for_stores_and_ingredients_price
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class UIMainWindow(QMainWindow):
    """Class for the window after user has logged in."""

    def __init__(self, user_name):
        """Initialize the object."""
        self.user_name = user_name
        self.create_recipe_instance = create_recipe_window_UI.CreateRecipeWindow()

        self.second_window = window_for_stores_and_ingredients_price.IngredientPrice()

        self.login_window = login_window.LoginWindow()

    def set_up_start_menu(self):
        """Set up the window."""
        self.db_instance = smartshop_mysql.SmartShopDB()
        super().__init__()
        # Get the path to the viewer folder
        viewer_path = Path(__file__).resolve().parent.parent

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI" / "start_menu.ui"
        loadUi(ui_file_path, self)

        self.start_up_window = self.findChild(QMainWindow, "mainwindow")

        self.recept_label = self.findChild(QLabel, "recept_label")
        self.recept_label.adjustSize()

        recipe_list = self.fill_up_recipe_list()
        self.ingredients_for_recipe = self.findChild(QComboBox, "chosen_recipe")
        self.ingredients_for_recipe.addItems(recipe_list)

        user_recipe_list = self.fill_up_recipe_list(self.user_name)
        self.user_ingredients_for_recipe = self.findChild(
            QComboBox, "your_chosen_recipe"
        )
        self.user_ingredients_for_recipe.addItems(user_recipe_list)

        self.get_ingredient_button = self.findChild(
            QPushButton, "get_ingredients_button"
        )
        self.get_ingredient_button.clicked.connect(
            lambda: self.get_ingredients(self.user_name)
        )

        self.user_get_ingredients_button = self.findChild(
            QPushButton, "your_get_ingredients_button"
        )
        self.user_get_ingredients_button.clicked.connect(
            lambda: self.user_get_ingredients(self.user_name)
        )

        self.create_recipe_button = self.findChild(QPushButton, "create_recipe_button")
        self.create_recipe_button.clicked.connect(
            lambda: self.create_recipe_window(self.user_name)
        )

        self.delete_recipe_button = self.findChild(QPushButton, "delete_recipe_button")
        self.delete_recipe_button.clicked.connect(
            lambda: self.delete_recipe(
                self.user_ingredients_for_recipe.currentText(), self.user_name
            )
        )

        self.logout_button = self.findChild(QPushButton, "logout_button")
        self.logout_button.clicked.connect(self.logout)

        self.show()

    def delete_recipe(self, recipe, user_name):
        """delete the chosen recipe."""
        if self.user_ingredients_for_recipe.currentText() != "":
            self.db_instance.delete_recipe(recipe, user_name)
            self.update_recipe_list(user_name)

    def update_recipe_list(self, user_name):
        """update the recipe list."""
        self.user_ingredients_for_recipe.clear()
        user_recipe_list = self.fill_up_recipe_list(user_name)
        self.user_ingredients_for_recipe.addItems(user_recipe_list)

    def fill_up_recipe_list(self, user_name=None):
        """Fill up the recipe list."""
        if not user_name:
            recipes = self.db_instance.get_recipe()
        else:
            recipes = self.db_instance.get_recipe(user_name)
        return recipes

    def create_recipe_window(self, user_name):
        """Hide current window and set up second window."""
        self.hide()
        self.create_recipe_instance.set_up_create_recipe_window(user_name)

    def user_get_ingredients(self, user_name):
        """Hide current window and set up second window."""
        if self.user_ingredients_for_recipe.currentText() == "":
            pass
        else:
            self.hide()
            self.second_window.set_up_ingredient_price_window(
                self, self.user_ingredients_for_recipe.currentText(), user_name
            )

    def get_ingredients(self, user_name):
        """Hide current window and set up second window."""
        self.hide()
        self.second_window.set_up_ingredient_price_window(
            self, self.ingredients_for_recipe.currentText(), user_name
        )

    def logout(self):
        """Open login_window."""
        self.hide()
        self.login_window.set_up_login()
