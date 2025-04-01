from src.class_product import Product


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_new_product():
    product_data = {
        "name": "Ноутбук",
        "description": "Игровой",
        "price": 100000.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert product.name == "Ноутбук"
    assert product.price == 100000.0


def test_price_validation():
    product = Product("Тест", "Тест", 100.0, 1)
    product.price = -50
    assert product.price == 100.0
    product.price = 200.0
    assert product.price == 200.0
