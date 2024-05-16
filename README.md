<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartShop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2, h3, h4, p {
            margin: 0 0 15px 0;
            line-height: 1.6;
        }
        ul, ol {
            margin: 0 0 15px 20px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow: auto;
        }
        .center {
            text-align: center;
        }
        .logo {
            width: 320px;
            margin: 0 auto 20px auto;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="center">
            <img class="logo" src="https://github.com/marcusgostasson/smartshop/assets/143846336/f1097435-1004-411d-8747-279634d3da42" alt="SmartShop Logo">
        </div>

        <h2>What is SmartShop</h2>
        <p><strong>SmartShop</strong> is a mobile app designed to help you save money on groceries by finding the cheapest recipes and ingredients. Whether you're an experienced cook or just starting out, SmartShop simplifies meal planning, price comparison, and creating budget-friendly shopping lists.</p>

        <h3>Features</h3>
        <ul>
            <li><strong>Recipe Discovery:</strong> Browse a large database of recipes tailored to your dietary needs, preferences, and budget, or create your own recipes.</li>
            <li><strong>Price Comparison:</strong> Get real-time price comparisons for ingredients from various grocery stores in your area.</li>
            <li><strong>Smart Shopping Lists:</strong> Generate shopping lists directly from recipes with a single tap, ensuring you have all necessary ingredients.</li>
            <li><strong>Weekly Meal Planning:</strong> Plan your meals for the week and always have the ingredients on hand to avoid unnecessary purchases.</li>
            <li><strong>Save Money:</strong> Discover the best deals and discounts on groceries to maximize your savings.</li>
        </ul>

        <h3>Get Started with SmartShop</h3>
        <ol>
            <li>Download the SmartShop app from the App Store: [link to App Store]</li>
            <li>Create an account or log in if you already have one.</li>
            <li>Set your location to see nearby stores or manually select your preferred grocery stores. [coming soon!]</li>
            <li>Start exploring delicious recipes and finding the best deals on your groceries!</li>
        </ol>

        <h3>Tips for Saving Money with SmartShop</h3>
        <ul>
            <li><strong>Seasonal Savvy:</strong> Look for recipes using seasonal ingredients, which are usually cheaper and fresher.</li>
            <li><strong>Bulk Up (if you can):</strong> Buy staples in bulk if you have the storage space and ensure you use them before they expire.</li>
            <li><strong>Deal Hunter:</strong> Utilize store sales and coupons integrated within the app to maximize your savings.</li>
            <li><strong>Plan It Out:</strong> Plan your meals in advance to avoid impulse purchases and unnecessary grocery trips.</li>
        </ul>

        <h3>Installation for Desktop App</h3>
        <h4>SSH</h4>
        <pre><code>git clone git@github.com:marcusgostasson/pigdicegame.git</code></pre>

        <h4>HTTPS</h4>
        <pre><code>git clone https://github.com/marcusgostasson/pigdicegame.git</code></pre>

        <h4>Add db.properties</h4>
        <p>Add a new file named <code>db.properties</code> under <code>requirements.txt</code> and paste this in, replacing <code>xxxxx</code> with your own <code>DB_USER</code> and <code>DB_PWD</code>:</p>
        <pre><code>DB_HOST=localhost
DB_SCHEMA=smartshop
DB_USER=xxxxx
DB_PWD=xxxxx</code></pre>

        <h4>Create a Schema in MySQL</h4>
        <p>Add this line to create a schema in MySQL:</p>
        <pre><code>CREATE SCHEMA smartshop;</code></pre>

        <h4>Copy the Database</h4>
        <p>Go to the codebase, copy the code from <code>smartshop_data_for_mysql</code>, and add it in MySQL.</p>

        <h4>Step-by-Step Guide to Using a Virtual Environment</h4>
        <h5>Step 1: Install the <code>venv</code> Module</h5>
        <p>If you're using Python 3.3 or later, the <code>venv</code> module is included. Check your Python version:</p>
        <ul>
            <li>On Windows: <code>python --version</code></li>
            <li>On macOS and Linux: <code>python3 --version</code></li>
        </ul>

        <h5>Step 2: Create a New Virtual Environment</h5>
        <ol>
            <li>Open your terminal or command prompt.</li>
            <li>Navigate to the directory where you want to create your virtual environment.</li>
            <li>Run the following command:
                <ul>
                    <li>On Windows: <pre><code>python -m venv .venv</code></pre></li>
                    <li>On macOS and Linux: <pre><code>python3 -m venv .venv</code></pre></li>
                </ul>
            </li>
        </ol>

        <h5>Step 3: Activate the Virtual Environment</h5>
        <p>To use the virtual environment, activate it:</p>
        <ul>
            <li>On Windows: <pre><code>.venv\Scripts\activate</code></pre></li>
            <li>On macOS and Linux: <pre><code>source .venv/bin/activate</code></pre></li>
        </ul>
        <p>The terminal prompt will change to indicate the active virtual environment (e.g., <code>(.venv)</code>).</p>

        <h5>Step 4: Install Packages</h5>
        <p>With the virtual environment activated, install packages with <code>pip</code>:</p>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h5>Step 5: Run the Program</h5>
        <p>Run the program:</p>
        <pre><code>make run</code></pre>

        <h5>Step 6: Deactivate the Virtual Environment</h5>
        <p>When finished, deactivate the virtual environment:</p>
        <pre><code>deactivate</code></pre>

        <h3>We hope you enjoy using SmartShop!</h3>

        <h4>FAQ</h4>
        <p><strong>Is SmartShop Free?</strong></p>
        <p>Yes, SmartShop is free to download and use! We offer a premium version with additional features, but the core functionality is free.</p>

        <p><strong>Which Stores Does SmartShop Support?</strong></p>
        <p>SmartShop supports most major grocery stores in your region. We're constantly expanding our reach to include more stores.</p>

        <h4>Feedback</h4>
        <p>We appreciate your input! For questions or suggestions, contact us at <a href="mailto:info@smartshop.com">info@smartshop.com</a></p>

        <h4>Additional Information</h4>
        <ul>
            <li>Visit our website: [link to website] (coming soon!)</li>
            <li>Follow us on social media for recipe inspiration and exclusive deals:
                <ul>
                    <li>Facebook: [link to Facebook page] (coming soon!)</li>
                    <li>Instagram: [link to Instagram page] (coming soon!)</li>
                </ul>
            </li>
        </ul>
    </div>
</body>
</html>
