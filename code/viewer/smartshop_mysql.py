import mysql.connector


class SMARTSHOP_DB:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="Smartshop")
            if self.db.is_connected():
                print("Successfully connected to database")
                self.mycursor = self.db.cursor()
        except mysql.connector.Error as e:
            print("Failed to connect to MySQL DB" + str(e))

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
