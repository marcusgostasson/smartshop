import smartshop_mysql
import window_for_stores_and_ingredients_price
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

from pathlib import Path


class UIMainWindow(QMainWindow):
    """Class for the window after user has logged in."""

    def __init__(self):
        """Initialize the object."""
        self.second_window = window_for_stores_and_ingredients_price.IngredientPrice()
        self.set_up_start_menu()

    def set_up_start_menu(self):
        """Set up the window."""
        self.db_instance = smartshop_mysql.SmartShopDB()
        super(UIMainWindow, self).__init__()
        # Get the path to the viewer folder
        viewer_path = Path(__file__).resolve().parent.parent

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI" / "start_menu.ui"
        loadUi(ui_file_path, self)

        self.start_up_window = self.findChild(QMainWindow, "mainwindow")

        self.logo_picture = self.findChild(QLabel, "logo1")
        logo_pixmap = QPixmap(f'{viewer_path}/pictures/smartshoplogo1.png')
        self.logo_picture.setPixmap(logo_pixmap)

        self.recept_label = self.findChild(QLabel, "recept_label")
        self.recept_label.adjustSize()

        self.ingredients_for_recipe = self.findChild(QComboBox, "chosen_recipe")
        self.recipes = self.db_instance.get_recipe()
        self.ingredients_for_recipe.addItems(self.recipes)
        self.ingredients_for_recipe.adjustSize()

        self.get_ingredients_button = self.findChild(QPushButton, "get_ingredients_button")
        self.get_ingredients_button.clicked.connect(self.get_ingredients)

        self.show()

    def get_ingredients(self):
        """Hide current window and set up second window."""
        self.hide()
        self.second_window.set_up_ingredient_price_window(self, self.ingredients_for_recipe.currentText())

    def closeEvent(self, event):
        """So the program stops running when you close the window."""
        sys.exit()
