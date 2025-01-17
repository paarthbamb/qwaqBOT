from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests
import time
import random
import threading

# Install required libraries:
# pip install selenium fake-useragent requests

# CAPTCHA Solving Service Configuration
CAPTCHA_API_KEY = "your_2captcha_api_key"  # Replace with your 2Captcha API key

def solve_captcha(api_key, site_key, url):
    """
    Solves CAPTCHA using 2Captcha API.
    :param api_key: Your 2Captcha API key
    :param site_key: CAPTCHA site key
    :param url: URL of the page with CAPTCHA
    :return: CAPTCHA solution token
    """
    # Request CAPTCHA solution
    response = requests.post(
        "http://2captcha.com/in.php",
        data={
            "key": api_key,
            "method": "userrecaptcha",
            "googlekey": site_key,
            "pageurl": url,
            "json": 1
        }
    )
    request_result = response.json()
    if request_result.get("status") != 1:
        print("CAPTCHA solution request failed.")
        return None
    
    # Poll for solution
    solution_id = request_result.get("request")
    while True:
        time.sleep(5)
        solution_response = requests.get(
            f"http://2captcha.com/res.php?key={api_key}&action=get&id={solution_id}&json=1"
        ).json()
        if solution_response.get("status") == 1:
            return solution_response.get("request")
        elif solution_response.get("request") == "CAPCHA_NOT_READY":
            print("Waiting for CAPTCHA solution...")
        else:
            print("Error solving CAPTCHA.")
            return None

# User-Agent Rotation
def get_random_user_agent():
    ua = UserAgent()
    return ua.random

# Proxy Support
def setup_driver_with_proxy(proxy):
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')  # Add proxy
    options.add_argument(f'user-agent={get_random_user_agent()}')  # Rotate User-Agent
    driver = webdriver.Chrome(options=options)
    return driver

# Task Function
def sneaker_task(product_url, proxy):
    driver = setup_driver_with_proxy(proxy)
    
    try:
        # Navigate to product page
        driver.get(product_url)
        print(f"Task started with proxy: {proxy}")
        time.sleep(3)  # Allow page to load
        
        # Select size
        try:
            size_button = driver.find_element(By.XPATH, "//button[contains(text(),'9')]")
            size_button.click()
            print("Size selected.")
        except Exception:
            print("Error selecting size. Moving on.")
        
        # Add to cart
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
        add_to_cart_button.click()
        print("Item added to cart.")
        time.sleep(2)
        
        # Solve CAPTCHA if detected
        if "captcha" in driver.page_source.lower():
            print("CAPTCHA detected. Solving...")
            site_key = "your_site_key"  # Replace with the actual CAPTCHA site key
            captcha_solution = solve_captcha(CAPTCHA_API_KEY, site_key, product_url)
            if captcha_solution:
                captcha_field = driver.find_element(By.ID, "g-recaptcha-response")
                driver.execute_script("arguments[0].style.display = 'block';", captcha_field)
                captcha_field.send_keys(captcha_solution)
                submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
                submit_button.click()
                print("CAPTCHA solved and submitted.")
            else:
                print("Failed to solve CAPTCHA.")
        
        # Proceed to checkout
        checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]")
        checkout_button.click()
        print("Proceeded to checkout.")
        
    except Exception as e:
        print(f"Error in task: {e}")
    finally:
        driver.quit()

# Multi-threading for Concurrent Tasks
def run_bot(product_url, proxies):
    threads = []
    
    for proxy in proxies:
        thread = threading.Thread(target=sneaker_task, args=(product_url, proxy))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# Main Execution
if __name__ == "__main__":
    # Example product URL
    product_url = "https://example.com/product-page"  # Replace with actual URL
    
    # List of proxies
    proxies = [
        "http://123.123.123.123:8080",
        "http://124.124.124.124:8080",
        "http://125.125.125.125:8080"
    ]
    
    run_bot(product_url, proxies)
