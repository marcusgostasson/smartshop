import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout, QHBoxLayout, QGridLayout

class ingredient_price(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingredienser för receptet")
        self.setGeometry(300, 300, 800, 200)

        self.total_cost = 0
        #self.product_prices = [] # så jag vet vilken label som är kopplad med spinbox
        self.store_and_products = {
            "ICA": [("Sås", 200), ("Bröd", 100), ("Ost", 150)],
            "COOP": [("Mjölk", 50), ("Mjöl", 55), ("Gurka", 20)],
            "WILLYS": [("Kaffe", 200), ("Mjölk", 90), ("Sås", 500)]
        }

        main_layout = QHBoxLayout(self)

        for store_name, products in self.store_and_products.items():
            store_layout = self.create_store_layout(store_name, products)
            main_layout.addLayout(store_layout)

        self.setLayout(main_layout)
        self.show()

    def create_store_layout(self, store_name, products):
        store_layout = QVBoxLayout()
        store_label = QLabel(store_name)
        store_layout.addWidget(store_label)

        grid_layout = QGridLayout()
        store_layout.addLayout(grid_layout)

        ingredient_header = QLabel("Produkt namn")
        grid_layout.addWidget(ingredient_header, 0, 0)

        price_header = QLabel("Pris")
        grid_layout.addWidget(price_header, 0, 1)

        quantity_label = QLabel("Antal")
        grid_layout.addWidget(quantity_label, 0, 2)

        row = 1
        self.total_cost = 0
        for product, price in products:
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

        self.total_cost_label = QLabel("Total kostnad: " + str(self.total_cost))
        grid_layout.addWidget(self.total_cost_label, row, 0)

        return store_layout

    def on_spinbox_changed(self, value, row, grid_layout):
        print(row, str(value), grid_layout)


app = QApplication(sys.argv)
window = ingredient_price()
sys.exit(app.exec_())
