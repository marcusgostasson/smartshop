"""Class for ingredient price."""

import sys
from pathlib import Path
import smartshop_mysql
import steps_for_recipe
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class IngredientPrice(QWidget):
    """Ingredient and price class."""

    def set_up_ingredient_price_window(self, start_menu, recipe_name, user_name):
        """Set up the window."""
        self.recipe_name = recipe_name
        self.user_name = user_name
        self.db_instance = smartshop_mysql.SmartShopDB()
        self.steps_for_chosen_recipe = steps_for_recipe.RecipeSteps()
        super().__init__()
        self.start_menu_window = start_menu

        self.setWindowTitle("Ingredienser för receptet")
        viewer_path = Path(__file__).resolve().parent.parent
        self.setWindowIcon(QIcon(f"{viewer_path}/pictures/smartshoplogo.png"))
        self.setGeometry(200, 200, 500, 200)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        recipe_price = self.db_instance.get_price_and_ingredients(recipe_name)

        self.lowest_total_cost = self.store_with_lowest_cost(recipe_price)

        main_layout = QHBoxLayout(self)
        for store_name, products in recipe_price.items():
            store_layout = self.create_store_layout(store_name, products)
            spacer = QSpacerItem(50, 100)
            main_layout.addItem(spacer)
            main_layout.addLayout(store_layout)
        spacer_for_grid = QSpacerItem(50, 50)
        main_layout.addSpacerItem(spacer_for_grid)

        vertical_layout = QVBoxLayout()
        main_layout.addLayout(vertical_layout)

        style = self.set_button_style()
        self.return_to_start_window_button = QPushButton(
            "   " + " Tillbaka till meny " + "  "
        )
        self.return_to_start_window_button.setStyleSheet(style)
        vertical_layout.addWidget(self.return_to_start_window_button)

        spacer_button = QSpacerItem(50, -325)
        vertical_layout.addSpacerItem(spacer_button)

        self.return_to_start_window_button.clicked.connect(self.return_to_start_window)

        self.get_steps_for_recipe_button = QPushButton(
            "  " + " Stegen till receptet " + "  "
        )
        self.get_steps_for_recipe_button.setStyleSheet(style)
        vertical_layout.addWidget(self.get_steps_for_recipe_button)
        self.get_steps_for_recipe_button.clicked.connect(self.create_recipe_step_window)

        self.setLayout(main_layout)
        self.show()

    def store_with_lowest_cost(self, recipe_price):
        """Calculate the store with the lowest cost."""
        lowest_total_cost = float("inf")
        for store_name, products in recipe_price.items():
            self.total_cost = 0
            for product in products:
                self.total_cost += product[3]
            if self.total_cost < lowest_total_cost:
                lowest_total_cost = self.total_cost
        return lowest_total_cost

    def create_store_layout(self, store_name, products):
        """Each store gets its own place in the gridlayout."""
        grid_layout = QGridLayout()
        store_label = QLabel()
        viewer_path = Path(__file__).resolve().parent.parent

        # Construct the path to the UI file relative to the viewer folder
        ui_file_path = viewer_path / "pictures"
        store_image = QPixmap(f"{ui_file_path}/{store_name}")
        store_image = store_image.scaled(200, 200)

        store_label.setPixmap(store_image)
        grid_layout.addWidget(store_label, 0, 0)

        ingredient_header = QLabel("Produkt namn")
        ingredient_header.setStyleSheet(
            "font-weight: bold; background-color: rgb(255, 255, 255);"
        )
        grid_layout.addWidget(ingredient_header, 1, 0)

        price_header = QLabel("Pris")
        price_header.setStyleSheet(
            "font-weight: bold; background-color: rgb(255, 255, 255);"
        )
        grid_layout.addWidget(price_header, 1, 1)

        self.row = 2
        self.total_cost = 0
        product_price = {}
        for product, amount, type, price in products:
            product_price[product] = price
            self.total_cost += price
            product_name_label = QLabel(f"{product} {amount} {type}")
            grid_layout.addWidget(product_name_label, self.row, 0)

            price_label = QLabel(str(price) + " kr")
            grid_layout.addWidget(price_label, self.row, 1)

            self.row += 1

        if self.total_cost == self.lowest_total_cost:
            self.total_cost_label = QLabel(f"Total kostnad: {self.total_cost:.2f}")
            self.total_cost_label.setStyleSheet(
                "font-weight: bold; color: green; font-size: 20px; background-color: rgb(255, 255, 255);"
            )
            grid_layout.addWidget(self.total_cost_label, self.row, 0)
            self.lowest_total_cost = self.total_cost
        else:
            self.total_cost_label = QLabel(f"Total kostnad: {self.total_cost:.2f}")
            self.total_cost_label.setStyleSheet(
                "font-weight: bold; background-color: rgb(255, 255, 255);"
            )
            grid_layout.addWidget(self.total_cost_label, self.row, 0)

        return grid_layout

    def create_recipe_step_window(self):
        """Hide current window and open steps for recipe window."""
        self.hide()
        self.steps_for_chosen_recipe.set_up_recipe_step_window(
            self.db_instance, self.recipe_name, self.start_menu_window, self.user_name
        )

    def return_to_start_window(self):
        """Hide current window and return to the start menu."""
        self.hide()
        self.start_menu_window.set_up_start_menu()

    def set_button_style(self):
        """Set the style for the buttons."""
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
