from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import smartshop_mysql
import window_for_stores_and_ingredients_price
import sys
from pathlib import Path


class UI_main_window(QMainWindow):
    def __init__(self):
        self.second_window = window_for_stores_and_ingredients_price.ingredient_price()
        self.set_up_start_menu()

    def set_up_start_menu(self):
        self.db_instance = smartshop_mysql.SMARTSHOP_DB()
        super(UI_main_window, self).__init__()
        # Get the path to the viewer folder
        viewer_path = Path(__file__).resolve().parent.parent / "viewer"

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "UI" / "start_menu.ui"

        # Load the UI file
        loadUi(ui_file_path, self)
        self.start_up_window = self.findChild(QMainWindow, "mainwindow")

        self.recept_label = self.findChild(QLabel, "recept_label")
        self.recept_label.adjustSize()

        self.ingredients_for_recipe = self.findChild(QComboBox, "chosen_recipe")
        self.recipes = self.db_instance.get_recipe()
        self.ingredients_for_recipe.addItems(self.recipes)

        self.get_ingredients_button = self.findChild(QPushButton, "get_ingredients_button")
        self.get_ingredients_button.clicked.connect(self.get_ingredients)

        self.show()

    def get_ingredients(self):
        self.hide()
        self.second_window.set_up_ingredient_price_window(self, self.ingredients_for_recipe.currentText())
            
    def closeEvent(self, event):
        """So the program stops running when you close the window."""
        sys.exit()

app = QApplication(sys.argv)
uiwindow = UI_main_window()
sys.exit(app.exec_())