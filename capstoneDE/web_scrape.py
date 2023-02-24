import random
from bs4 import BeautifulSoup
import requests
from capstoneDE.generate_ids import generate_ids


def webscrape_product_data(url_list):

    data = []

    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_items = soup.find_all('div', class_='product-thumb-details', limit=20)
        product_type = soup.find ('h1', class_='js-fixed-header').text


        for item in product_items:
            product_id = generate_ids()
            product_type = product_type
            product_name = item.find ('span', class_='product-thumb-title').text.replace ('\n', '')
            product_price = item.find ('span', class_='product-thumb-price').text.replace ('\n', '')
            stock_quantity = random.randint(0, 100)
            data.append([product_id, product_type, product_name, product_price, stock_quantity])

    return data
