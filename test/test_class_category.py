from src.class_category import Category
from src.class_product import Product

# Старые тесты


def test_category_initialization():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])
    assert "Телефон" in category.products


def test_add_product():
    product = Product("Xiaomi", "Смартфон", 20000.0, 8)
    category = Category("Телефоны", "Мобильные", [])
    category.add_product(product)
    assert "Xiaomi" in category.products

# Новые тесты по заданию 3


def test_category_str():
    p1 = Product("A", "Desc", 100.0, 2)
    p2 = Product("B", "Desc", 200.0, 3)
    category = Category("Test", "Desc", [p1, p2])
    assert str(category) == "Test, количество продуктов: 5 шт."


def test_empty_category_str():
    category = Category("Empty", "Desc", [])
    assert str(category) == "Empty, количество продуктов: 0 шт."
