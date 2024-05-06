from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from pathlib import Path
import smartshop_mysql
import login_window
import start_window
from functools import partial


class CreateRecipeWindow(QWidget):
    def set_up_create_recipe_window(self, user_name):
        self.login_window = login_window.LoginWindow()
        self.start_window = start_window.UIMainWindow(user_name)
        self.db_instance = smartshop_mysql.SmartShopDB()

        super(CreateRecipeWindow, self).__init__()
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
        self.search_ingrediense = self.findChild(QPushButton, "search_ingredient_button")
        self.search_ingrediense.clicked.connect(self.handle_search)

        self.back_to_start_wind = self.findChild(QPushButton, "back_to_start_wind")
        self.back_to_start_wind.clicked.connect(lambda: self.back_to_start_window(user_name))

        self.add_ingredient_button = self.findChild(QPushButton, "add_ingrediense_button")
        self.add_ingredient_button.clicked.connect(lambda: self.add_ingredient(self.ingrediense_box.currentText()))
        self.ingrediense_list = []

        self.create_recipe_button = self.findChild(QPushButton, "create_recipe_button")
        self.create_recipe_button.clicked.connect(lambda: self.create_recipe(user_name))

        self.show()

    def back_to_start_window(self, user_name):
        """back to start window"""
        self.hide()
        start_window.UIMainWindow(user_name)

    def create_recipe(self, user_name):
        does_recipe_exist = self.db_instance.get_recipe_name(self.recipe_name.text())
        if does_recipe_exist:
            self.login_window.error_message("Namnet på ditt recept finns redan, välj ett annat")

        elif self.recipe_name.text() == "":
            self.recipe_name.setText("No name")
            self.db_instance.insert_user_recipe(self.recipe_name.text(), user_name, self.recipe_steps.toPlainText(), self.ingrediense_list)
            self.hide()
            start_window.UIMainWindow(user_name)
        else:
            self.db_instance.insert_user_recipe(self.recipe_name.text(), user_name, self.recipe_steps.toPlainText(), self.ingrediense_list)
            self.hide()
            start_window.UIMainWindow(user_name)

    def add_ingredient(self, ingrediense):
        if ingrediense in self.ingrediense_list:
            pass
        else:
            product_id = self.db_instance.get_product_id(ingrediense)
            self.ingrediense_list.append(product_id)
            ingredient = QLabel(ingrediense)
            self.box.layout().addWidget(ingredient)

    def handle_search(self):
        product_name = self.user_product_choice.text()
        ingredients = self.db_instance.get_ingrediense(product_name)
        self.ingrediense_box.clear()
        self.ingrediense_box.addItems(ingredients)
