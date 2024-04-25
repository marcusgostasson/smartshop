import mysql.connector


class SMARTSHOP_DB:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root123!",
                database="smartshop")
            if self.db.is_connected():
                print("Successfully connected to database")
                self.mycursor = self.db.cursor()
        except mysql.connector.Error as e:
            print("Failed to connect to MySQL DB" + str(e))

    def create_user(self, first_name, last_name, username_create,
                    email, hashed_password):
        """Send user to MySQL."""

        self.mycursor.execute("""INSERT INTO user (user_name, password,
                               first_name,last_name, email) VALUES
                                   (%s, %s, %s, %s, %s)""", (username_create,
                                                             hashed_password,
                                                             first_name,
                                                             last_name,
                                                             email))

        self.db.commit()

    def get_username_and_password(self, username, hashed_password):
        """Get username and password from database."""
        self.mycursor.execute("""SELECT user_name, password
                              FROM user
                              WHERE user_name = %s and password = %s""",
                              (username, hashed_password))
        username_password = self.mycursor.fetchall()
        return username_password


    def get_recipe_step(self, recipe_name):
        self.mycursor.execute("SELECT recipe_step FROM recipe WHERE recipe_name = %s", (recipe_name,))
        recipe_steps = self.mycursor.fetchall()
        if recipe_steps:
            return recipe_steps
        return None

    def get_product_and_price(self, recipe_name):
        self.mycursor.execute("SELECT product_name, product_price FROM recipe, product, ingredients_recipe WHERE recipe_name = %s AND recipe_id = recipe_recipe_id and product_id = product_product_id", (recipe_name,))
        product_and_price = self.mycursor.fetchall()
        # See if can make it into a dictionary when returning
        # Vi vet ju recepten så kanske en query för product namn convert till list sen en för product price
        # convert till list sen får ju de en varsin column en i taget
        return product_and_price
