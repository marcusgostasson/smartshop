from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import smartshop_mysql
import steps_for_recipe
from pathlib import Path
import sys


class IngredientPrice(QWidget):
    """Ingredient and price class."""

    def set_up_ingredient_price_window(self, start_menu, recipe_name, user_name):
        """Set up the window."""
        self.recipe_name = recipe_name
        self.user_name = user_name
        self.db_instance = smartshop_mysql.SmartShopDB()
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
            spacer = QSpacerItem(100, 200)
            main_layout.addItem(spacer)
            main_layout.addLayout(store_layout)

        style = self.set_button_style()
        return_to_start_window_button = QPushButton("Tillbaka till meny")
        return_to_start_window_button.setStyleSheet(style)
        main_layout.addWidget(return_to_start_window_button)
        return_to_start_window_button.clicked.connect(self.return_to_start_window)

        get_steps_for_recipe_button = QPushButton("Stegen till receptet")
        get_steps_for_recipe_button.setStyleSheet(style)
        main_layout.addWidget(get_steps_for_recipe_button)
        get_steps_for_recipe_button.clicked.connect(self.create_recipe_step_window)

        self.setLayout(main_layout)
        self.show()

    def store_with_lowest_cost(self, recipe_price):
        """Calculate the store with the lowest cost."""
        lowest_total_cost = float("inf")
        for store_name, products in recipe_price.items():
            self.total_cost = 0
            for product in products:
                self.total_cost += product[1]
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
        for product, price, portionsize in products:
            product_price[product] = price
            # eller kan jag har i varje loop här en dictionary med key är produkt namn sen value är price sen med spinboxen ta * med priset sen när jag ska ta total kost så går jag igenom dictionaryn
            # sen i funktionen så tar jag vilken ingrediens från label och sätter jag value för den nycklen i dict med spinbox value gånger priset
            # sen vet jag inte om det blir fel med att ingredienserna heter ju samma men olika butiker men då kanske ta primarykey eller det som är unikt
            # sen bara jämföra om primary keyn är samma som "labelns namn" i dictionaryn
            self.total_cost += price
            product_name_label = QLabel(product)
            grid_layout.addWidget(product_name_label, self.row, 0)

            price_label = QLabel(str(price) + " kr")
            grid_layout.addWidget(price_label, self.row, 1)

            # eller kan man skicka med totalkostnads labeln för den gridlayouten och vilken price label som ligger till vänster av spinboxen
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
        self.steps_for_chosen_recipe = steps_for_recipe.RecipeSteps()
        self.steps_for_chosen_recipe.set_up_recipe_step_window(
            self.db_instance, self.recipe_name, self.start_menu_window, self.user_name
        )

    def return_to_start_window(self):
        """Hide current window and return to the start menu."""
        self.hide()
        self.start_menu_window.set_up_start_menu()

    def closeEvent(self, event):
        """So the program stops running when you close the window."""
        sys.exit()

    def set_button_style(self):
        """Set the style for the buttons."""
        button_style = """QPushButton {
    border-style: solid;
    border-color: #9999aa;
    border-radius: 25px; /* Adjust border-radius to half of min-height for QPushButton */
    color: white;
    background-color: #3474eb;
    min-width: 150px;
    min-height: 50px;
}

QPushButton:enabled {
    background-color: #2C65A4;
    color: white;
}

QPushButton:pressed {
    background-color: #0d2f72;
    color: #fffffe;
}

QPushButton:hover:!pressed {
    background-color: #0034AB;
    color: white;
}

QPushButton:disabled {
    background-color: #aaaaaa;
    color: #ffffff;
}
"""
        return button_style
