from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from pathlib import Path
import smartshop_mysql


class CreateRecipeWindow(QWidget):
    def set_up_create_recipe_window(self, user_name):
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

        self.user_product_choice = self.findChild(QLineEdit, "type_in_recipe")
        self.ingrediense_box = self.findChild(QComboBox, "ingrediense_box")
        self.search_ingrediense = self.findChild(QPushButton, "search_ingredient_button")
        self.search_ingrediense.clicked.connect(self.handle_search)

        self.add_ingredient_button = self.findChild(QPushButton, "add_ingrediense_button")
        self.add_ingredient_button.clicked.connect(lambda: self.add_ingredient(self.ingrediense_box.currentText()))

        self.create_recipe_button = self.findChild(QPushButton, "create_recipe_button")
        self.create_recipe_button.clicked.connect(lambda: self.create_recipe(user_name))

        self.show()

    def add_ingredient(self, ingrediense):
        ingredient = QLabel(ingrediense)
        self.box.layout().addWidget(ingredient)  # Add the label to the layout of the scroll area's content widget
        
    def handle_search(self):
        product_name = self.user_product_choice.text()
        ingredients = self.db_instance.get_ingrediense(product_name)
        self.ingrediense_box.clear()
        self.ingrediense_box.addItems(ingredients)
