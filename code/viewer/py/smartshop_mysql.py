import mysql.connector
from jproperties import Properties


class SmartShopDB:
    """Smartshop database class."""

    def __init__(self):
        """Initialize the connection to the smartshop database."""
        configs = Properties()
        with open("db.properties", "rb") as config_file:
            configs.load(config_file)
        host = configs.get("DB_HOST").data
        user = configs.get("DB_USER").data
        password = configs.get("DB_PWD").data
        database = configs.get("DB_SCHEMA").data
        try:
            self.db = mysql.connector.connect(
                host=host, user=user, password=password, database=database
            )
            if self.db.is_connected():
                print("Successfully connected to database")
                self.mycursor = self.db.cursor()
        except mysql.connector.Error as e:
            print("Failed to connect to MySQL DB" + str(e))

    def get_price_and_ingredients(self, recipe_name):
        """Fetch all ingredients and the price for the selected recipe."""
        self.mycursor.execute(
            """
SELECT store.store_name, product.product_name, product.product_amount, product.product_amount_type, product_price_for_each_store.product_price
FROM recipe
JOIN ingredients_recipe ON recipe.recipe_id = ingredients_recipe.recipe_recipe_id
JOIN product ON ingredients_recipe.product_product_id = product.product_id
JOIN product_price_for_each_store ON product.product_id = product_price_for_each_store.p_product_id
JOIN store ON product_price_for_each_store.store_store_id = store.store_id
WHERE recipe.recipe_name = %s; """,
            (recipe_name,),
        )
        recipe_ingredient = self.mycursor.fetchall()
        organized_data = {}

        for store, product_name, amount, type, price in recipe_ingredient:
            if store not in organized_data:
                organized_data[store] = []
            organized_data[store].append((product_name, amount, type, price))
        return organized_data

    def delete_recipe(self, recipe, user_name):
        """Delete the chosen recipe."""
        self.mycursor.execute(
            "SELECT recipe_id FROM recipe WHERE recipe_name = %s", (recipe,)
        )
        recipe_id = self.mycursor.fetchone()
        self.mycursor.execute(
            "DELETE FROM ingredients_recipe WHERE recipe_recipe_id= %s", (recipe_id[0],)
        )

        self.mycursor.execute(
            """DELETE FROM recipe
                                WHERE user_user_name = %s AND recipe_name = %s""",
            (user_name, recipe),
        )
        self.db.commit()

    def get_recipe(self, user_name=None):
        """Fetch all the recipes that exists."""
        if not user_name:
            self.mycursor.execute(
                "SELECT recipe_name FROM recipe WHERE user_user_name IS NULL"
            )
        else:
            self.mycursor.execute(
                "SELECT recipe_name FROM recipe WHERE user_user_name = %s", (user_name,)
            )
        recipe_names = self.mycursor.fetchall()
        recipes = []
        for recipe in recipe_names:
            for rec in recipe:
                recipes.append(rec)
        return recipes

    def get_ingrediense(self, product_name):
        if not product_name:
            return []
        self.mycursor.execute(
            "SELECT product_name, product_amount, product_amount_type FROM product WHERE product_name LIKE %s",
            ("%" + product_name + "%",),
        )
        all_ingrediense = self.mycursor.fetchall()
        ingredienses = []
        for ingrediense in all_ingrediense:
            ingrediense_name, amount, type = ingrediense
            label_name = f"{ingrediense_name} {amount} {type}"
            ingredienses.append(label_name)
        return ingredienses

    def get_steps_for_recipe(self, recipe_name):
        """Fetch the steps for the selected recipe."""
        self.mycursor.execute(
            "SELECT recipe_step FROM recipe WHERE recipe_name = %s", (recipe_name,)
        )
        steps = self.mycursor.fetchone()
        for step in steps:
            return step

    def create_user(self, first_name, last_name, username_create, email, hashed_pass):
        """Send user to MySQL."""

        self.mycursor.execute(
            """INSERT INTO user (user_name, password,
                               first_name,last_name, email) VALUES
                                   (%s, %s, %s, %s, %s)""",
            (username_create, hashed_pass, first_name, last_name, email),
        )

        self.db.commit()

    def get_username_data_base(self, username):
        """Get the username from database."""
        self.mycursor.execute(
            """SELECT user_name
                                 FROM user
                                 WHERE user_name = %s""",
            (username,),
        )
        data_base_username = self.mycursor.fetchall()
        if not data_base_username:
            return None
        return data_base_username[0][0]

    def get_password_hash(self, username):
        """Get password hash from database for a given username."""
        try:
            self.mycursor.execute(
                """SELECT password
                                     FROM user
                                     WHERE user_name = %s""",
                (username,),
            )
            username_password = self.mycursor.fetchone()
            if username_password:
                return username_password[0]
        except Exception as e:
            print("Database query failed:", e)
            return None

    def get_recipe_name(self, recipe_name):
        self.mycursor.execute(
            "SELECT recipe_name FROM recipe WHERE recipe_name = %s", (recipe_name,)
        )
        result = self.mycursor.fetchone()
        if result is not None:
            return True
        else:
            return False

    def insert_user_recipe(
        self, recipe_name, user_name, recipe_steps, ingrediense_list
    ):
        self.mycursor.execute(
            "INSERT INTO recipe(recipe_name, recipe_step, user_user_name) VALUES(%s, %s, %s)",
            (recipe_name, recipe_steps, user_name),
        )

        self.mycursor.execute("SELECT LAST_INSERT_ID()")
        recipe_id = self.mycursor.fetchone()[0]

        for ingredient in ingrediense_list:
            self.mycursor.execute(
                "INSERT INTO ingredients_recipe(product_product_id, recipe_recipe_id) VALUES(%s, %s)",
                (ingredient, recipe_id),
            )
            self.db.commit()

    def get_product_id(self, ingrediens):

        self.mycursor.execute(
            "SELECT product_id FROM product WHERE product_name = %s", (ingrediens,)
        )
        product_id = self.mycursor.fetchone()
        return product_id[0]
