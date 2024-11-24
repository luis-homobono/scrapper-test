from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(options=options)

def search(url):
    driver.get(url)
    time.sleep(5)
    product_containers = driver.find_elements(By.CLASS_NAME, "vtex-product-summary-2-x-container")
    products = []
    for product in product_containers:  # Limitar a los primeros 10
        try:
            name = product.find_element(By.CLASS_NAME, "vtex-product-summary-2-x-productBrand").text
            prices = product.find_elements(By.CLASS_NAME, "tiendasjumboqaio-jumbo-minicart-2-x-price")
            if prices:
                if len(prices) > 1:
                    products.append({"name": name, "price": prices[1].text, "promo_price": prices[0].text})
                else:
                    products.append({"name": name, "price": prices[0].text})
        except Exception as e:
            print(f"Error al procesar producto: {e}")
            continue

    return products
