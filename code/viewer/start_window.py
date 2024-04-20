from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import smartshop_mysql
import window_for_stores_and_ingredients_price
import sys


class UI_main_window(QMainWindow):
    def __init__(self):
        self.db_instance = smartshop_mysql.SMARTSHOP_DB()
        super(UI_main_window, self).__init__()
        loadUi("smartshop/code/viewer/start_menu.ui", self)

        self.ingredients_for_recipe = self.findChild(QComboBox, "chosen_recipe")

        self.get_ingredients_button = self.findChild(QPushButton, "get_ingredients_button")
        self.get_ingredients_button.clicked.connect(self.get_ingredients)

        #self.print_hi = self.findChild(QPushButton, "get_recipe_button")
        #self.print_hi.clicked.connect(self.print_recipe)

        #self.recipe = self.findChild(QLabel, "recipe_step")
        #self.chosen_recipe = self.findChild(QComboBox, "chosen_recipe")

        self.show()

    def get_ingredients(self):
        self.close()
        ingredients_for_chosen_recipe = self.ingredients_for_recipe.currentText()
        #self.ingredient_menu = ingredients_gui.UI_ingredient_menu(self.db_instance, ingredients_for_chosen_recipe)
        self.ingredient_price_window = window_for_stores_and_ingredients_price.ingredient_price(self.db_instance, ingredients_for_chosen_recipe)

        #self.db_instance.get_ingredients()

    def print_recipe(self):
        recipe_step = self.db_instance.get_recipe_step(self.chosen_recipe.currentText())
        if recipe_step is None:
            self.recipe.setText("No steps for this recipe")
        else:
            self.recipe.setText(recipe_step[0][0])
            self.recipe.adjustSize()


app = QApplication(sys.argv)
uiwindow = UI_main_window()
app.exec_()
