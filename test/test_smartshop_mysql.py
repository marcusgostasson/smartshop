"""
import unittest
import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))
from smartshop.code.py import smartshop_mysql


class TestSmartshopMysql(unittest.TestCase):

    def test_get_price_and_ingredients_for_taco(self):
        db_instance = smartshop_mysql.SmartShopDB()
        taco_res = db_instance.get_price_and_ingredients("tacos")
        taco_ingredients = {'Willys': [('Ost', 200.0, 'G', 31.34), ('Lök', 200.0, 'G', 7.22), ('Sallad', 200.0, 'G', 12.83),
                                       ('Tomat', 500.0, 'G', 96.99), ('Tacoskal', 12.0, 'ST', 47.63), ('Nötfärs-20%', 500.0, 'G', 53.81)],
                            'Ica': [('Ost', 200.0, 'G', 91.89), ('Lök', 200.0, 'G', 97.8), ('Sallad', 200.0, 'G', 78.96), ('Tomat', 500.0, 'G', 63.66),
                                    ('Tacoskal', 12.0, 'ST', 19.2), ('Nötfärs-20%', 500.0, 'G', 17.65)],
                            'Coop': [('Ost', 200.0, 'G', 42.71), ('Lök', 200.0, 'G', 27.25), ('Sallad', 200.0, 'G', 93.99),
                                     ('Tomat', 500.0, 'G', 7.1), ('Tacoskal', 12.0, 'ST', 16.13), ('Nötfärs-20%', 500.0, 'G', 78.14)]}
        self.assertEqual(taco_res, taco_ingredients)

    def test_get_price_and_ingredients_for_hamburger(self):
        db_instance = smartshop_mysql.SmartShopDB()
        hamburger_res = db_instance.get_price_and_ingredients("hamburgare")
        hamburger_ingredients = {'Willys': [('Ost', 200.0, 'G', 31.34), ('Lök', 200.0, 'G', 7.22),
                                            ('Sallad', 200.0, 'G', 12.83), ('Tomat', 500.0, 'G', 96.99),
                                            ('Hamburgerbröd', 6.0, 'ST', 19.05), ('Nötfärs-20%', 500.0, 'G', 53.81)],
                                 'Ica': [('Ost', 200.0, 'G', 91.89), ('Lök', 200.0, 'G', 97.8), ('Sallad', 200.0, 'G', 78.96),
                                         ('Tomat', 500.0, 'G', 63.66), ('Hamburgerbröd', 6.0, 'ST', 0.17), ('Nötfärs-20%', 500.0, 'G', 17.65)],
                                 'Coop': [('Ost', 200.0, 'G', 42.71), ('Lök', 200.0, 'G', 27.25), ('Sallad', 200.0, 'G', 93.99),
                                          ('Tomat', 500.0, 'G', 7.1), ('Hamburgerbröd', 6.0, 'ST', 27.27), ('Nötfärs-20%', 500.0, 'G', 78.14)]}

        self.assertEqual(hamburger_res, hamburger_ingredients)

    def test_get_price_and_ingredients_for_kyckling_roma(self):
        db_instance = smartshop_mysql.SmartShopDB()
        kyckling_roma_res = db_instance.get_price_and_ingredients("kyckling roma")
        kyckling_roma_ingredients = {'Coop': [('Kycklingbröstfile', 500.0, 'G', 80.53)],
                                     'Ica': [('Kycklingbröstfile', 500.0, 'G', 59.78)],
                                     'Willys': [('Kycklingbröstfile', 500.0, 'G', 57.29)]}
        self.assertEqual(kyckling_roma_res, kyckling_roma_ingredients)

    def test_get_price_and_ingredients_for_pasta_med_räkor_och_curry(self):
        db_instance = smartshop_mysql.SmartShopDB()
        pasta_med_räkor_och_curry_res = db_instance.get_price_and_ingredients("pasta med räkor och curry")
        pasta_med_räkor_och_curry_ingredients = {'Willys': [('Sallad', 200.0, 'G', 12.83), ('Tomat', 500.0, 'G', 96.99),
                                                            ('Pastasås', 400.0, 'DL', 12.06), ('Pasta', 500.0, 'G', 91.01)],
                                                 'Ica': [('Sallad', 200.0, 'G', 78.96), ('Tomat', 500.0, 'G', 63.66),
                                                         ('Pastasås', 400.0, 'DL', 11.02), ('Pasta', 500.0, 'G', 58.98)],
                                                 'Coop': [('Sallad', 200.0, 'G', 93.99), ('Tomat', 500.0, 'G', 7.1),
                                                          ('Pastasås', 400.0, 'DL', 81.01), ('Pasta', 500.0, 'G', 1.29)]}
        self.assertEqual(pasta_med_räkor_och_curry_res, pasta_med_räkor_och_curry_ingredients)

    def test_get_recipe(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_recipe()
        recipes_exp = ['Pasta med räkor och curry',
                       'Hamburgare',
                       'Tacos',
                       'Kyckling Roma']
        self.assertEqual(res, recipes_exp)

        res2 = db_instance.get_recipe("test")
        recipes_exp2 = ['test recept']
        self.assertEqual(res2, recipes_exp2)

    def test_get_steps_for_recipe_for_hamburgare(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Hamburgare")
        exp = 1. Stek nötfärs.
2. Rosta hamburgerbullar.
3. Montera burgare med sallad, tomat, lök och ost.
        self.assertEqual(res, exp)

    def test_get_steps_for_recipe_for_tacos(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Tacos")
        exp = "1. Stek nötfärs med tacokrydda. \n2. Värm tacoskal. \n3. Montera tacos med nötkött, sallad, tomat, lök och ost."
        self.assertEqual(res, exp)

    def test_get_steps_for_recipe_for_kyckling_roma(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Kyckling Roma")
        exp = 1. Marinera kycklingbröst.
2. Grilla tills den är genomstekt.
        self.assertEqual(res, exp)

    def test_get_steps_for_recipe_for_pasta_med_räkor_och_curry(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Pasta med räkor och curry")
        exp = 1. Koka upp vatten.
2. Tillsätt pasta.
3. Koka tills al dente.
4. Dränera.
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()

"""
