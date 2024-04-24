from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import smartshop_mysql


class ingredient_price(QWidget):
    def __init__(self):
        pass

    def set_up_ingredient_price_window(self, start_menu, recipe_name):
        self.db_instance = smartshop_mysql.SMARTSHOP_DB()
        super().__init__()
        self.start_menu_window = start_menu
        self.setWindowTitle("Ingredienser för receptet")
        self.setGeometry(300, 300, 800, 200)

        self.total_cost = 0
        #self.product_prices = [] # så jag vet vilken label som är kopplad med spinbox
        #self.store_and_products = {
         #   "ica.png": [("Sås", 200, 2), ("Bröd", 100, 2), ("Ost", 150, 2)],
         #   "coop.png": [("Mjölk", 50, 2), ("Mjöl", 55, 2), ("Gurka", 20, 2)],
         #   "willys.png": [("Kaffe", 200, 2), ("Mjölk", 90, 2), ("Sås", 500, 2)]
        #}
        recipe_price = self.db_instance.get_recipe_step(recipe_name)
        self.lowest_total_cost = float('inf')
        for store_name, products in recipe_price.items():
            self.total_cost = 0
            for product in products:
                self.total_cost += product[1]
            if self.total_cost < self.lowest_total_cost:
                self.lowest_total_cost = self.total_cost

        main_layout = QHBoxLayout(self)
        self.col_for_store_name = 0
        for store_name, products in recipe_price.items():
            store_layout = self.create_store_layout(store_name, products)
            spacer = QSpacerItem(100, 200)
            main_layout.addItem(spacer)
            main_layout.addLayout(store_layout)

        return_to_start_window_button = QPushButton("Tillbaka till meny")
        main_layout.addWidget(return_to_start_window_button, self.row)
        return_to_start_window_button.clicked.connect(self.return_to_start_window)

        self.setLayout(main_layout)
        self.show()

    def create_store_layout(self, store_name, products):
        #store_layout = QVBoxLayout()
        font = QFont()
        font.setBold(True)
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
        ingredient_header.setFont(font)
        grid_layout.addWidget(ingredient_header, 1, 0)

        price_header = QLabel("Pris")
        price_header.setFont(font)
        grid_layout.addWidget(price_header, 1, 1)

        #quantity_label = QLabel("Antal")
        #grid_layout.addWidget(quantity_label, 1, 2)

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
            #self.product_prices.append(price_label)

            #spinbox = QSpinBox()
            #spinbox.setFixedWidth(50)
            #spinbox.setMaximum(999)
            #spinbox.setMinimum(0)
            #spinbox.setValue(1)
            #grid_layout.addWidget(spinbox, self.row, 2)

            #spinbox.valueChanged.connect(lambda value, row=self.row, grid_layout=grid_layout: self.on_spinbox_changed(value * price, row, grid_layout)) # eller om man kör en sql query som tar antalet i spinboxen?
            # eller kan man skicka med totalkostnads labeln för den gridlayouten och vilken price label som ligger till vänster av spinboxen
            self.row += 1

        if self.total_cost == self.lowest_total_cost:
            self.total_cost_label = QLabel(f"Total kostnad: {self.total_cost:.2f}")
            self.total_cost_label.setStyleSheet("font-weight: bold; color: green;")
            grid_layout.addWidget(self.total_cost_label, self.row, 0)
            self.lowest_total_cost = self.total_cost
        else:
            self.total_cost_label = QLabel(f"Total kostnad: {self.total_cost:.2f}")
            self.total_cost_label.setStyleSheet("font-weight: bold;")
            grid_layout.addWidget(self.total_cost_label, self.row, 0)

        return grid_layout
    
    def return_to_start_window(self):
        self.destroy()
        self.start_menu_window.set_up_start_menu()

    def on_spinbox_changed(self, value, row, grid_layout, price, total_cost_label):
        print("Row:", row, "Value:", value, "Price:", price)
        # Update the total cost label
        new_total_cost = self.total_cost - price + (value * price)
        self.total_cost_label.setText("Total cost: " + str(new_total_cost))
        self.total_cost = new_total_cost