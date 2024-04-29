import mysql.connector
from jproperties import Properties


class SmartShopDB:
    """Smartshop database class."""

    def __init__(self):
        """Initialize the connection to the smartshop database."""
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
        """Fetch all ingredients and the price for the selected recipe."""
        self.mycursor.execute("""
SELECT store.store_name , product.product_name , product.product_price, ingredients_recipe.portionsize
FROM ingredients_recipe
JOIN store on store.store_id=ingredients_recipe.store_store_id
JOIN recipe on recipe.recipe_id=ingredients_recipe.recipe_recipe_id
JOIN product on product.product_id=ingredients_recipe.product_product_id
WHERE recipe.recipe_name= %s; """, (recipe_name,))
        recipe_ingredient = self.mycursor.fetchall()
        organized_data = {}

        for store, product, price, portionsize in recipe_ingredient:
            if store not in organized_data:
                organized_data[store] = []
            organized_data[store].append((product, price, portionsize))
        return organized_data

    def get_recipe(self):
        """Fetch all the recipes that exists."""
        self.mycursor.execute("SELECT recipe_name from recipe")
        recipe_names = self.mycursor.fetchall()
        recipes = []
        for recipe in recipe_names:
            for rec in recipe:
                recipes.append(rec)
        return recipes

    def get_steps_for_recipe(self, recipe_name):
        """Fetch the steps for the selected recipe."""
        self.mycursor.execute("SELECT recipe_step FROM recipe WHERE recipe_name = %s", (recipe_name,))
        steps = self.mycursor.fetchone()
        for step in steps:
            return step

    def create_user(self, first_name, last_name, username_create,
                    email, hashed_pass):
        """Send user to MySQL."""

        self.mycursor.execute("""INSERT INTO user (user_name, password,
                               first_name,last_name, email) VALUES
                                   (%s, %s, %s, %s, %s)""", (username_create,
                                                             hashed_pass,
                                                             first_name,
                                                             last_name,
                                                             email))

        self.db.commit()

    def get_username_data_base(self, username):
        """Get the username from database."""
        self.mycursor.execute("""SELECT user_name
                                 FROM user
                                 WHERE user_name = %s""", (username,))
        data_base_username = self.mycursor.fetchall()
        if not data_base_username:
            return None
        return data_base_username[0][0]

    def get_password_hash(self, username):
        """Get password hash from database for a given username."""
        try:
            self.mycursor.execute("""SELECT password
                                     FROM user
                                     WHERE user_name = %s""", (username,))
            username_password = self.mycursor.fetchone()
            if username_password:
                return username_password[0]
        except Exception as e:
            print("Database query failed:", e)
            return None