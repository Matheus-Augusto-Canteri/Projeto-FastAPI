import json
from product import Product

def generate_products():
    f = open('./data/products.json')
    data = json.loads(f.read())
    f.close()
    return data