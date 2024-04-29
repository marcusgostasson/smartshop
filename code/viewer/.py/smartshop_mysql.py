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

    # Functions
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
        """Get the username from database"""
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
