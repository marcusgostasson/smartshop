<p align="center">
    <img width="320" alt="smartshoplogo" src="https://github.com/marcusgostasson/smartshop/assets/143846336/f1097435-1004-411d-8747-279634d3da42">
</p>

# What is SmartShop

**SmartShop** is a mobile app designed to help you save money on groceries by finding the cheapest recipes and ingredients. Whether you're an experienced cook or just starting out, SmartShop simplifies meal planning, price comparison, and creating budget-friendly shopping lists.

## Features

- **Recipe Discovery:** Browse a large database of recipes tailored to your dietary needs, preferences, and budget, or create your own recipes.
- **Price Comparison:** Get real-time price comparisons for ingredients from various grocery stores in your area.
- **Smart Shopping Lists:** Generate shopping lists directly from recipes with a single tap, ensuring you have all necessary ingredients.
- **Weekly Meal Planning:** Plan your meals for the week and always have the ingredients on hand to avoid unnecessary purchases.
- **Save Money:** Discover the best deals and discounts on groceries to maximize your savings.

## Get Started with SmartShop

1. Download the SmartShop app from the App Store: *(coming soon!)*
2. Create an account or log in if you already have one.
3. Set your location to see nearby stores or manually select your preferred grocery stores. *(Coming soon!)*
4. Start exploring delicious recipes and finding the best deals on your groceries!

## Tips for Saving Money with SmartShop

- **Seasonal Savvy:** Look for recipes using seasonal ingredients, which are usually cheaper and fresher.
- **Bulk Up (if you can):** Buy staples in bulk if you have the storage space and ensure you use them before they expire.
- **Deal Hunter:** Utilize store sales and coupons integrated within the app to maximize your savings.
- **Plan It Out:** Plan your meals in advance to avoid impulse purchases and unnecessary grocery trips.

## Installation for Desktop App

### SSH

```sh
git clone git@github.com:marcusgostasson/pigdicegame.git
```

### HTTPS

```sh
git clone https://github.com/marcusgostasson/pigdicegame.git
```

### Add db.properties

Create a new file named `db.properties` under `requirements.txt` and paste the following content, replacing `xxxxx` with your own `DB_USER` and `DB_PWD`:

```
DB_HOST=localhost
DB_SCHEMA=smartshop
DB_USER=xxxxx
DB_PWD=xxxxx
```

### Create a Schema in MySQL

Add this line to create a schema in MySQL:

```sql
CREATE SCHEMA smartshop;
```

### Copy the Database

Go to the codebase, copy the code from `smartshop_data_for_mysql`, and add it in MySQL.

### Step-by-Step Guide to Using a Virtual Environment

#### Step 1: Install the `venv` Module

If you're using Python 3.3 or later, the `venv` module is included. Check your Python version:

- On Windows:
  ```sh
  python --version
  ```
- On macOS and Linux:
  ```sh
  python3 --version
  ```

#### Step 2: Create a New Virtual Environment

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create your virtual environment.
3. Run the following command:
   - On Windows:
     ```sh
     python -m venv .venv
     ```
   - On macOS and Linux:
     ```sh
     python3 -m venv .venv
     ```
   where `.venv` is the name of the virtual environment. You can choose any name you like.

#### Step 3: Activate the Virtual Environment

To use the virtual environment, activate it:

- On Windows:
  ```sh
  .venv\Scripts\activate
  ```
- On macOS and Linux:
  ```sh
  source .venv/bin/activate
  ```

The terminal prompt will change to indicate the active virtual environment (e.g., `(.venv)`).

#### Step 4: Install Packages

With the virtual environment activated, install packages with `pip`:

```sh
pip install -r requirements.txt
```

#### Step 5: Run the Program

Run the program:

```sh
make run
```

#### Step 6: Deactivate the Virtual Environment

When finished, deactivate the virtual environment:

```sh
deactivate
```

## We hope you enjoy using SmartShop!

## FAQ

**Is SmartShop Free?**

Yes, SmartShop is free to download and use! We offer a premium version with additional features, but the core functionality is free.

**Which Stores Does SmartShop Support?**

SmartShop supports most major grocery stores in your region. We're constantly expanding our reach to include more stores.

## Feedback

We appreciate your input! For questions or suggestions, contact us at [info@smartshop.com](mailto:info@smartshop.com)

## Additional Information

- Visit our website: [link to website] *(Coming soon!)*
- Follow us on social media for recipe inspiration and exclusive deals:
  - Facebook: [link to Facebook page] *(Coming soon!)*
  - Instagram: [link to Instagram page] *(Coming soon!)*
