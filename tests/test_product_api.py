import requests
from product import Product

BASE_URL = 'http://127.0.0.1:8000' 

def test_should_get_list_of_products():
    response = requests.get(f'{BASE_URL}/products')
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) >= 1 

def test_should_insert_new_product():
    product = {"name": "Mouse Gamer", "price": 250.0}
    response = requests.post(f'{BASE_URL}/products', json=product)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "inserted"

def test_should_have_new_product_after_insert():
    response = requests.get(f'{BASE_URL}/products')
    products = response.json()["products"]
    names = [product["name"] for product in products]
    assert "Mouse Gamer" in names

def test_should_not_accept_invalid_product():
    invalid_product = {"name": "Teclado Mecânico", "price": "caro"}
    response = requests.post(f'{BASE_URL}/products', json=invalid_product)
    assert response.status_code == 422  

def test_product_price_should_be_positive():
    response = requests.get(f'{BASE_URL}/products')
    products = response.json()["products"]
    for product in products:
        assert product["price"] > 0
