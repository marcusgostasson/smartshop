<p align="center">
    <img width="320" alt="smartshoplogo" src="https://github.com/marcusgostasson/smartshop/assets/143846336/f1097435-1004-411d-8747-279634d3da42">
</p>

**What is SmartShop**

SmartShop is a mobile app that helps you save money on groceries by finding the cheapest recipes and ingredients. Whether you're a seasoned cook or just starting out, SmartShop makes it easy to plan your meals, compare prices at nearby stores, and create shopping lists that won't break the bank.

**Features**

* **Recipe Discovery:** Search through a vast database of recipes based on your dietary needs, preferences, and budget and create your own recipe.
* **Price Comparison:** See real-time price comparisons for ingredients from different grocery stores in your area.
* **Smart Shopping Lists:** Build your shopping list directly from recipes with a single tap. No more scrambling for ingredients or forgetting something essential.
* **Weekly Meal Planning:**  Plan your meals for the week and ensure you always have the ingredients on hand to avoid impulse purchases.
* **Save Money:** SmartShop helps you find the best deals and discounts on groceries, so you can stretch your budget further.


**Get Started with SmartShop**

1. Download the SmartShop app from the App Store: [link to App Store].
2. Create an account or log in if you already have one.
3. Set your location to see nearby stores or manually select your preferred grocery stores. [coming soon!]
4. Start exploring delicious recipes and finding the best deals on your groceries!


**Tips for Saving Money with SmartShop**

* **Seasonal Savvy:**  Search for recipes that use seasonal ingredients, which are typically cheaper and fresher.
* **Bulk Up (if you can):**  Consider buying in bulk for staples if you have the storage space. Just make sure you'll use it all before it expires.
* **Deal Hunter:**  Take advantage of store sales and coupons integrated within the app to maximize your savings.
* **Plan It Out:**  Plan your meals ahead of time to avoid impulse purchases and unnecessary grocery trips.

* **Installation**

***SSH
```
git@github.com:marcusgostasson/pigdicegame.git
```
***HTTPS
```
https://github.com/marcusgostasson/pigdicegame.git
```

Att skapa en virtuell miljö (virtual environment eller `venv`) är ett vanligt sätt att hantera beroenden i Python-projekt. Här är en steg-för-steg-guide för att skapa och använda en `venv`:

### Steg 1: Installera `venv`-modulen
Om du använder en modern version av Python (3.3 eller senare), kommer `venv`-modulen redan vara inkluderad. Annars kan du behöva installera den. Du kan kontrollera din Python-version med:
```
python --version
```sh
eller
```sh
python3 --version
```

### Steg 2: Skapa en ny virtuell miljö
1. Öppna din terminal eller kommandoprompt.
2. Navigera till den katalog där du vill skapa din virtuella miljö.
3. Kör följande kommando:
   ```sh
   python -m venv .venv
   ```
   eller
   ```sh
   python3 -m venv .venv
   ```
   där `.venv` är namnet på den virtuella miljön. Du kan välja vilket namn du vill.

### Steg 3: Aktivera den virtuella miljön
För att använda den virtuella miljön, behöver du aktivera den.

- På Windows:
  ```sh
  myenv\Scripts\activate
  ```

- På macOS och Linux:
  ```sh
  source myenv/bin/activate
  ```

När miljön är aktiverad, kommer terminalprompten att ändras för att indikera att du arbetar inom den virtuella miljön (vanligtvis ser du namnet på miljön inom parentes, t.ex. `(.venv)`).

### Steg 4: Installera paket
Nu när din virtuella miljö är aktiverad, kan du installera paket med `pip` som vanligt. Till exempel:
```sh
pip install requirements.txt
```

### Steg 5: Avaktivera den virtuella miljön
När du är färdig med att använda den virtuella miljön, kan du avaktivera den genom att köra:
```sh
deactivate
```

### Ytterligare tips
  ```
- För att installera alla beroenden från en `requirements.txt`-fil i en ny `venv`:
  ```sh
  pip install -r requirements.txt
  ```

Genom att använda `venv` kan du hantera beroenden för olika projekt utan att de påverkar varandra, vilket är särskilt användbart i utvecklingsmiljöer.

**We hope you enjoy using SmartShop!**

**FAQ**

* **Is SmartShop Free?**

Yes, SmartShop is free to download and use!  We offer a premium version with additional features, but the core functionality remains free.

* **Which Stores Does SmartShop Support?**

SmartShop supports most major grocery stores in your region. We're constantly working on expanding our reach to include even more stores.

**Feedback**

We appreciate your input! If you have any questions or suggestions, please feel free to contact us at [info@smartshop.com]


**Additional Information**

* Visit our website: [link to website] (coming soon!)
* Follow us on social media for recipe inspiration and exclusive deals:
    * Facebook: [link to Facebook page] (coming soon!)
    * Instagram: [link to Instagram page] (coming soon!)
