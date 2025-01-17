# qwaqBOT
fully-working sneaker bot developed to assist in reselling business. utilizes python, particularly selenium.

the bot uses **2Captcha API** for captcha solving. this will only work if you have a valid **2Captcha** account and api key. some websites may have complex captcha systems (e.g., **reCAPTCHA v3**, dynamic **CAPTCHAs**) that **2Captcha** may not be able to solve, which could cause the bot to fail.

the bot relies on specific **XPaths** to interact with website elements (e.g., adding a product to the cart or proceeding to checkout). these **XPaths** are unique to each website, so they must be modified to fit the html structure of the targeted website. if the **XPaths** are incorrect, or if the website layout changes, the bot will not function as intended.

proxies are required to rotate ips to prevent getting blocked by websites. the bot uses **fake-useragent** for rotating **user-agents** to simulate different browsers. some websites may use more sophisticated bot detection methods (e.g., browser fingerprinting), so proxy rotation and **user-agent** manipulation might not be enough.

the bot uses **Selenium** to automate interactions with web pages. while this is an effective method for interacting with websites, it can be detected by sites that use anti-bot measures. to avoid detection, you will need to fine-tune browser settings, such as disabling headless mode or adding extra logic to simulate human-like behavior.

the bot uses **threading** to manage multiple tasks concurrently. this is important for tasks like bypassing queues and managing checkout processes. make sure to manage thread synchronization and ensure that no race conditions occur, especially during the checkout process.

the bot currently doesn't handle the checkout process, so you will need to integrate this functionality based on the specific website you're targeting.

**always** be aware of the legal and ethical implications of using a bot.


**what you need to do before using this bot:**
1. install required dependencies:
   install python 3.x.
   install the following python libraries:
   ```bash
   pip install selenium requests 2captcha fake_useragent

2. set up your 2captcha account:
   sign up at [2Captcha](https://2captcha.com/), and get an api key.
   replace `'YOUR_2CAPTCHA_API_KEY'` in the code with your actual api key.

3. modify xpaths:
   customize the **XPaths** used in the code to match the product page and checkout process of the site you want to target.
   use browser tools (like chrome devtools) to inspect the elements and find the appropriate **XPaths**.

4. set up proxy and user-agent rotation:
   for proxies, you can use services like **BrightData**, **ScraperAPI**, or any proxy service with support for rotating ips.
   the bot uses the **fake-useragent** library to simulate different browsers, but you may want to implement more sophisticated user-agent rotation.

5. test the bot:
   before using the bot on live websites, **test** it in a safe, non-production environment.
   make sure the bot interacts with the website as expected, including adding products to the cart and proceeding to checkout.

**disclaimer**: this bot is for **educational purposes only**. always respect the terms of service of websites you interact with and ensure that your actions comply with local laws and regulations. the use of bots for purchasing items in bulk may be illegal or unethical in some regions.


