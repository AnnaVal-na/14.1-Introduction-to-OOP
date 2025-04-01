from src.class_category import Category
from src.class_product import Product


def test_category_initialization():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    assert "Телефон" in category.products
    assert "Ноутбук" in category.products


def test_add_product():
    Category.product_count = 0
    product = Product("Xiaomi", "Смартфон", 20000.0, 8)
    category = Category("Телефоны", "Мобильные", [])
    category.add_product(product)

    assert Category.product_count == 1
    assert "Xiaomi" in category.products


def test_private_products_access():
    product = Product("Test", "Test", 100.0, 1)
    category = Category("Test", "Test", [product])
    assert hasattr(category, "_Category__products")
    assert len(category._Category__products) == 1
