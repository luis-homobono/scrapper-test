import json
from typing import List
from dataclasses import dataclass

import pandas as pd

url = 'https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json'
file = './data.json'

@dataclass
class Product:
    allergens: List
    sku: str
    vegan: bool
    kosher: bool
    organic: bool
    vegetarian: bool
    gluten_free: bool
    lactose_free: bool
    package_quantity: int
    unit_size: int
    net_weight: int

def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


data = get_data()
all_variants = data['allVariants']

attributes_values = []

for variant in all_variants:
    values = [attributes for attributes in variant['attributesRaw'] if attributes['name'] == 'custom_attributes']
    attributes_values += values

products = []
for attributes in attributes_values:
    values = json.loads(attributes['value']['en-CR'])
    product = Product(
        allergens=[value['name'] for value in values['allergens']['value']],
        sku=values['sku']['value'],
        vegan=values['vegan']['value'],
        kosher=values['kosher']['value'],
        organic=values['organic']['value'],
        vegetarian=values['vegetarian']['value'],
        gluten_free=values['gluten_free']['value'],
        lactose_free=values['lactose_free']['value'],
        package_quantity=values['package_quantity']['value'],
        unit_size=values['unit_size']['value'],
        net_weight=values['net_weight']['value'],
    )
    products.append(product)

products_df = pd.DataFrame(products)

products_df.to_csv()
