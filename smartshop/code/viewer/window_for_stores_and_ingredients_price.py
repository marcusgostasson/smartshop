from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import smartshop_mysql
import window_for_stores_and_ingredients_price
import sys


class ingredient_price(QWidget):
    def __init__(self, db_instance, chosen_recipe):
        super().__init__()
        self.setWindowTitle("Ingredienser för receptet")
        self.setGeometry(300, 300, 800, 200)

        self.total_cost = 0
        #self.product_prices = [] # så jag vet vilken label som är kopplad med spinbox
        self.store_and_products = {
            "ica.png": [("Sås", 200), ("Bröd", 100), ("Ost", 150)],
            "coop.png": [("Mjölk", 50), ("Mjöl", 55), ("Gurka", 20)],
            "willys.png": [("Kaffe", 200), ("Mjölk", 90), ("Sås", 500)]
        }
        self.lowest_total_cost = float('inf')
        for store_name, products in self.store_and_products.items():
            self.total_cost = 0
            for product in products:
                self.total_cost += product[1]
            if self.total_cost < self.lowest_total_cost:
                self.lowest_total_cost = self.total_cost

        main_layout = QHBoxLayout(self)
        self.col_for_store_name = 0
        for store_name, products in self.store_and_products.items():
            store_layout = self.create_store_layout(store_name, products)
            main_layout.addLayout(store_layout)

        self.setLayout(main_layout)
        self.show()

    def create_store_layout(self, store_name, products):
        #store_layout = QVBoxLayout()
        
        grid_layout = QGridLayout()
        store_label = QLabel()
        store_image = QPixmap("smartshop/code/viewer/pictures/" + store_name)
        store_image = store_image.scaled(200, 200)

        store_label.setPixmap(store_image)
        #store_label.resize(100,100)
        grid_layout.addWidget(store_label, 0, self.col_for_store_name)

        #grid_layout = QGridLayout()
        #store_layout.addLayout(grid_layout)

        ingredient_header = QLabel("Produkt namn")
        grid_layout.addWidget(ingredient_header, 1, 0)

        price_header = QLabel("Pris")
        grid_layout.addWidget(price_header, 1, 1)

        quantity_label = QLabel("Antal")
        grid_layout.addWidget(quantity_label, 1, 2)

        row = 2
        self.total_cost = 0
        product_price = {}
        for product, price in products:
            product_price[product] = price
            # eller kan jag har i varje loop här en dictionary med key är produkt namn sen value är price sen med spinboxen ta * med priset sen när jag ska ta total kost så går jag igenom dictionaryn
            # sen i funktionen så tar jag vilken ingrediens från label och sätter jag value för den nycklen i dict med spinbox value gånger priset
            # sen vet jag inte om det blir fel med att ingredienserna heter ju samma men olika butiker men då kanske ta primarykey eller det som är unikt
            # sen bara jämföra om primary keyn är samma som "labelns namn" i dictionaryn
            self.total_cost += price
            product_name_label = QLabel(product)
            grid_layout.addWidget(product_name_label, row, 0)

            price_label = QLabel(str(price))
            grid_layout.addWidget(price_label, row, 1)
            #self.product_prices.append(price_label)

            spinbox = QSpinBox()
            spinbox.setFixedWidth(50)
            spinbox.setMaximum(999)
            spinbox.setMinimum(0)
            spinbox.setValue(1)
            grid_layout.addWidget(spinbox, row, 2)

            spinbox.valueChanged.connect(lambda value, row=row, grid_layout=grid_layout: self.on_spinbox_changed(value * price, row, grid_layout)) # eller om man kör en sql query som tar antalet i spinboxen?
            # eller kan man skicka med totalkostnads labeln för den gridlayouten och vilken price label som ligger till vänster av spinboxen
            row += 1

        if self.total_cost == self.lowest_total_cost:
            self.total_cost_label = QLabel("Total kostnad: " + str(self.total_cost))
            self.total_cost_label.setStyleSheet("font-weight: bold; color: green;")
            grid_layout.addWidget(self.total_cost_label, row, 0)
            self.lowest_total_cost = self.total_cost
        else:
            self.total_cost_label = QLabel("Total kostnad: " + str(self.total_cost))
            self.total_cost_label.setStyleSheet("font-weight: bold;")
            grid_layout.addWidget(self.total_cost_label, row, 0)

        return grid_layout

    def on_spinbox_changed(self, value, row, grid_layout, price, total_cost_label):
        print("Row:", row, "Value:", value, "Price:", price)
        # Update the total cost label
        new_total_cost = self.total_cost - price + (value * price)
        self.total_cost_label.setText("Total cost: " + str(new_total_cost))
        self.total_cost = new_total_cost
