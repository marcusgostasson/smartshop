import unittest
import sys
from unittest.mock import patch, MagicMock

sys.path.append("C:/Users/Razmu/agile_development/SmartShop/smartshop/code/viewer")

import smartshop_mysql


class TestSmartshopMysql(unittest.TestCase):

    def test_get_price_and_ingredients_for_taco(self):
        db_instance = smartshop_mysql.SMARTSHOP_DB()
        taco_res = db_instance.get_price_and_ingredients("tacos")
        taco_ingredients = {'Willys': [('Taco Kryddmix Original Mild', 10.9, 2), ('Körsbärstomater Klass 1', 14.9, 2),
                                        ('Blandfärs 20%', 49.9, 2), ('Smör Normalsaltat 82%', 59.9, 2)],
                            'Ica': [('Taco Kryddmix Original Mild', 10.95, 2), ('Körsbärstomater Klass 1', 22.95, 2),
                                    ('Blandfärs 21%', 51.95, 2), ('Smör Normalsaltat 82%', 59.95, 2)], 
                            'Coop': [('Taco Kryddmix Original Mild', 11.95, 2), ('Körsbärstomater Hela', 16.5, 2),
                                    ('Nötfärs 12%', 58.95, 2), ('Smör Normalsaltat 82%', 59.95, 2)]}
        self.assertEqual(taco_res, taco_ingredients)

    def test_get_price_and_ingredients_for_hamburger(self):
        db_instance = smartshop_mysql.SMARTSHOP_DB()
        hamburger_res = db_instance.get_price_and_ingredients("hamburger")
        hamburger_ingredients = {'Willys': [('Blandfärs 20%', 49.9, 2), ('Salt Finkornigt', 7.9, 2),
                                            ('Svart Peppar Mellan Malen', 19.9, 2), ('Hamburgerbröd Frisco 4-p', 23.9, 2),
                                            ('Hamburgerost Cheddarsmak', 22.9, 2), ('Extra Virgin Fruttato Olivolja', 48.9, 2)],
                                 'Ica': [('Blandfärs 21%', 51.95, 2), ('Salt Finkornigt', 10.5, 2), ('Svart Peppar Mellan Malen', 24.5, 2),
                                         ('Hamburgerbröd Frisco 4-p', 23.95, 2), ('Hamburgerost Cheddarsmak', 22.95, 2),
                                         ('Extra Virgin Olivolja', 55.95, 2)],
                                 'Coop': [('Nötfärs 12%', 58.95, 2), ('Salt Finkornigt', 8.95, 2), ('Svart Peppar Malen', 27.95, 2),
                                          ('Hamburgerbröd Frisco 4-p', 23.9, 2), ('Hamburgerost Cheddarsmak', 32.5, 2),
                                          ('Olivolja Extra Virgin', 85.95, 2)]}
        self.assertEqual(hamburger_res, hamburger_ingredients)


if __name__ == '__main__':
    unittest.main()
