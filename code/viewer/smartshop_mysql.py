import mysql.connector
from jproperties import Properties


class SMARTSHOP_DB:
    def __init__(self):
        configs = Properties()
        with open('db.properties', 'rb') as config_file:
            configs.load(config_file)
        host = configs.get("DB_HOST").data
        user = configs.get("DB_USER").data
        password = configs.get("DB_PWD").data
        database = configs.get("DB_SCHEMA").data
        try:
            self.db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
            if self.db.is_connected():
                print("Successfully connected to database")
                self.mycursor = self.db.cursor()
        except mysql.connector.Error as e:
            print("Failed to connect to MySQL DB" + str(e))

    def get_price_and_ingredients(self, recipe_name):
        #self.mycursor.execute("SELECT recipe_step FROM recipe WHERE recipe_name = %s", (recipe_name,))
        #recipe_steps = self.mycursor.fetchall()
        #if recipe_steps:
        #return recipe_steps
        #return None
        self.mycursor.execute("""select store.store_name , product.product_name , product.product_price, ingredients_recipe.portionsize 
from ingredients_recipe
join store on store.store_id=ingredients_recipe.store_store_id
join recipe on recipe.recipe_id=ingredients_recipe.recipe_recipe_id
join product on product.product_id=ingredients_recipe.product_product_id
Where recipe.recipe_name= %s; """, (recipe_name,))
        recipe_ingredient = self.mycursor.fetchall()
        organized_data = {}

        for store, product, price, portionsize in recipe_ingredient:
            if store not in organized_data:
                organized_data[store] = []
            organized_data[store].append((product, price, portionsize))
        return organized_data

        #for store, products in organized_data.items():
        #    print(store)
        #    for product, price, port in products:
        #        print(f"\t{product}: {price} SEK, {port} portioner")

    def get_recipe(self):
        self.mycursor.execute("SELECT recipe_name from recipe")
        recipe_names = self.mycursor.fetchall()
        recipes = []
        for recipe in recipe_names:
            for rec in recipe:
                recipes.append(rec)
        return recipes
    
    def get_steps_for_recipe(self, recipe_name):
        self.mycursor.execute("SELECT recipe_step FROM recipe WHERE recipe_name = %s", (recipe_name,))
        steps = self.mycursor.fetchall()
        for step in steps:
            for s in step:
                return s
