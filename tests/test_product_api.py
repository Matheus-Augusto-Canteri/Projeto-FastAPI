import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

client = TestClient(app)

def test_should_get_list_of_products():
    response = client.get('/products')
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) >= 1

def test_should_insert_new_product():
    product = {"name": "Mouse Gamer", "price": 250.0}
    response = client.post('/products', json=product)
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "inserted"

def test_should_have_new_product_after_insert():
    # First insert a test product
    test_product = {"name": "Test Product", "price": 100.0}
    client.post('/products', json=test_product)
    
    # Then verify it exists
    response = client.get('/products')
    products = response.json()["products"]
    names = [product["name"] for product in products]
    assert "Test Product" in names

def test_should_not_accept_invalid_product():
    invalid_product = {"name": "Teclado Mecânico", "price": "caro"}
    response = client.post('/products', json=invalid_product)
    assert response.status_code == 422

def test_product_price_should_be_positive():
    response = client.get('/products')
    products = response.json()["products"]
    for product in products:
        assert product["price"] > 0