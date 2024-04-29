import unittest
import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))
from smartshop.code.viewer.py import smartshop_mysql


class TestSmartshopMysql(unittest.TestCase):

    def test_get_price_and_ingredients_for_taco(self):
        db_instance = smartshop_mysql.SmartShopDB()
        taco_res = db_instance.get_price_and_ingredients("tacos")
        taco_ingredients = {'Willys': [('Taco Kryddmix Original Mild', 10.9, 2), ('Körsbärstomater Klass 1', 14.9, 2),
                                       ('Blandfärs 20%', 49.9, 2), ('Smör Normalsaltat 82%', 59.9, 2)],
                            'Ica': [('Taco Kryddmix Original Mild', 10.95, 2), ('Körsbärstomater Klass 1', 22.95, 2),
                                    ('Blandfärs 21%', 51.95, 2), ('Smör Normalsaltat 82%', 59.95, 2)], 
                            'Coop': [('Taco Kryddmix Original Mild', 11.95, 2), ('Körsbärstomater Hela', 16.5, 2),
                                     ('Nötfärs 12%', 58.95, 2), ('Smör Normalsaltat 82%', 59.95, 2)]}
        self.assertEqual(taco_res, taco_ingredients)

    def test_get_price_and_ingredients_for_hamburger(self):
        db_instance = smartshop_mysql.SmartShopDB()
        hamburger_res = db_instance.get_price_and_ingredients("hamburgare")
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

    def test_get_price_and_ingredients_for_kyckling_roma(self):
        db_instance = smartshop_mysql.SmartShopDB()
        kyckling_roma_res = db_instance.get_price_and_ingredients("kyckling roma")
        kyckling_roma_ingredients = {'Willys': [('Körsbärstomater Klass 1', 14.9, 2),
                                                ('Pasta Spaghetti', 22.9, 2),
                                                ('Svart Peppar Mellan Malen', 19.9, 2),
                                                ('Kycklingfile Fryst', 99.9, 2),
                                                ('Salvia', 19.9, 2), ('Extra Virgin Fruttato Olivolja', 48.9, 2),
                                                ('Charlotten Lök', 17.9, 2), ('Matlagningsvin Vitt 2.2%', 29.5, 2),
                                                ('Strösocker', 21.9, 2), ('Zucchini', 14.9, 2), ('Parmigiano Reggiano Riven', 24.9, 2)],
                                     'Ica': [('Körsbärstomater Klass 1', 22.95, 2), ('Pasta Spaghetti', 22.95, 2),
                                             ('Svart Peppar Mellan Malen', 24.5, 2), ('Kycklingfile Fryst', 99.95, 2),
                                             ('Salvia', 24.95, 2), ('Extra Virgin Olivolja', 55.95, 2), ('Charlotten Lök', 22.95, 2),
                                             ('Matlagningsvin Vitt 2.2%', 39.5, 2), ('Strösocker', 25.5, 2), ('Zucchini', 18.48, 2),
                                             ('Parmigiano Reggiano Riven', 38.95, 2)],
                                     'Coop': [('Körsbärstomater Hela', 16.5, 2), ('Pasta Spaghetti', 23.5, 2),
                                              ('Svart Peppar Malen', 27.95, 2), ('Kycklingfile Fryst', 116.0, 2), ('Salvia Eko', 24.95, 2),
                                              ('Olivolja Extra Virgin', 85.95, 2), ('Charlotten Lök', 14.95, 2), ('Matlagningsvin Vitt 2%', 35.95, 2),
                                              ('Strösocker', 27.95, 2), ('Zucchini', 14.95, 2), ('Parmigiano Reggiano Riven', 24.5, 2)]}
        self.assertEqual(kyckling_roma_res, kyckling_roma_ingredients)

    def test_get_price_and_ingredients_for_pasta_med_räkor_och_curry(self):
        db_instance = smartshop_mysql.SmartShopDB()
        pasta_med_räkor_och_curry_res = db_instance.get_price_and_ingredients("pasta med räkor och curry")
        pasta_med_räkor_och_curry_ingredients = {'Willys': [('Pasta Spaghetti', 22.9, 2), ('Stora Skalade Räkor', 59.9, 2),
                                                            ('Gul Lök', 14.9, 2), ('Vit Lök', 3.9, 2), ('Spetspaprika Röd', 21.9, 2),
                                                            ('Champinjoner', 17.9, 2), ('Smör Normalsaltat 82%', 59.9, 2), ('Curry', 19.9, 2),
                                                            ('Kokos Mjölk', 13.9, 2), ('Salt Finkornigt', 7.9, 2), ('Chilisås', 21.9, 2),
                                                            ('Sambal Olek', 25.9, 2)],
                                                 'Ica': [('Pasta Spaghetti', 22.95, 2),('Stora Skalade Räkor', 58.95, 2),
                                                         ('Gul Lök', 19.95, 2), ('Vit Lök', 12.95, 2), ('Spetspaprika Röd', 21.95, 2),
                                                         ('Champinjoner', 18.95, 2), ('Smör Normalsaltat 82%', 59.95, 2),
                                                         ('Curry', 24.5, 2), ('Kokos Mjölk', 12.95, 2), ('Salt Finkornigt', 10.5, 2),
                                                         ('Chilisås', 21.95, 2), ('Sambal Olek', 18.5, 2)],
                                                 'Coop': [('Pasta Spaghetti', 23.5, 2), ('Räkor Extra Stora Skalade', 81.95, 2),
                                                          ('Gul Lök', 14.95, 2), ('Vit Lök', 5.45, 2), ('Paprika Snack Röd', 29.95, 2),
                                                          ('Champinjoner', 21.95, 2), ('Smör Normalsaltat 82%', 59.95, 2), ('Curry', 23.5, 2),
                                                          ('Kokos Mjölk', 16.5, 2), ('Salt Finkornigt', 8.95, 2), ('Chilisås', 24.95, 2), ('Sambal Olek', 26.5, 2)]}
        self.assertEqual(pasta_med_räkor_och_curry_res, pasta_med_räkor_och_curry_ingredients)

    def test_get_recipe(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_recipe()
        recipes_exp = ['Hamburgare',
                       'Kyckling Roma',
                       'Pasta med räkor och curry',
                       'Tacos']
        self.assertEqual(res, recipes_exp)

    def test_get_steps_for_recipe_for_hamburgare(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Hamburgare")
        exp = """1. Blanda ihop färsen och kryddorna och forma till fyra puckar. 
2. Stek eller grilla burgarna snabbt på hög värme tills de har fått fin färg på båda sidor. 
3. Sänk värmen och stek eller grilla färdigt till önskad stekgrad. För medium 3–4 minuter per sida. 
4. Hamburgerdressing: Rör ihop majonnäs, yoghurt, saltgurka, vitlök och ketchup. 
Smaka av med salt, peppar och några droppar worcestershiresås. 
5. Karamelliserad lök: Skiva löken och stek i smör eller olja. 
Tillsätt en nypa socker och stek tills den är rejält gyllenbrun. Då får löken en söt och mild smak. 
6. Rosta bröden lätt och lägg på valfria tillbehör som dressing, sallad, tomat, lök och ost. """
        self.assertEqual(res, exp)

    def test_get_steps_for_recipe_for_tacos(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Tacos")
        exp = """1. Tvätta limen och riv skalet. Pressa ur saften och blanda med skal, honung, vatten och salt. 
Skala, dela och skiva lökarna tunt. Vänd runt dem i lagen och låt dra, 30 minuter. 
2. Stek färsen smulig i smör i stekpanna. Rör i tacokrydda, tärnade tomater och vatten. Småkoka 5 minuter. 
3. Tärna gurkan. Blanda crème fraiche med riven vitlök. Lägg lite sallad i tacoskalen och fyll på med färs, majs och gurka. 
Toppa med crème fraiche och picklad lök."""
        self.assertEqual(res, exp)

    def test_get_steps_for_recipe_for_kyckling_roma(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Kyckling Roma")
        exp = """1. Stek kyckling tillsammans med salvia­blad i lite av oljan. 
Lägg över på en tallrik medan du gör tomatsåsen. 
2. Fräs löken genomskinlig i resten av oljan. Tillsätt vinet och låt det mesta koka in. 
Blanda ner tomater, socker, salt och peppar och låt puttra 5–10 minuter. 
3. Koka pastan tillsammans med squash­en och låt det rinna av. 
4. Blanda såsen med pastan, squashen, kycklingen och det mesta av parme­sanosten. 
Lägg upp i djupa, gärna för­ värmda tallrikar och strö över resten av osten. 
Ta några drag med pepparkvarnen över."""
        self.assertEqual(res, exp)

    def test_get_steps_for_recipe_for_pasta_med_räkor_och_curry(self):
        db_instance = smartshop_mysql.SmartShopDB()
        res = db_instance.get_steps_for_recipe("Pasta med räkor och curry")
        exp = """1. Koka pastan enligt beskrivningen på paketet. Skala räkorna. 
Stek lök, vitlök, paprika och svamp i smör tillsammans med curry i en stor stekpanna. 
2. Lägg över i en gryta och häll i kokosmjölk, chilisås och sambal oelek. Låt sjuda 3 minuter. 
3. Tillsätt räkorna. 
4. Servera med kokt pasta. Garnera med strimlad salladslök och färsk timjan."""
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
