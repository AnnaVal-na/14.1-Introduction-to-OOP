from src.class_category import Category
from src.class_product import Product


def test_category_initialization():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])
    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2
    assert isinstance(category.products[0], Product)
    assert isinstance(category.products[1], Product)


def test_category_count_increment():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("p1", "desc", 100.0, 1)
    p2 = Product("p2", "desc", 200.0, 2)
    category = Category("Cat1", "Desc", [p1, p2])
    assert category.name == "Cat1"
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("p3", "desc", 300.0, 3)
    category = Category("Cat2", "Desc", [p3])
    assert category.name == "Cat2"
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_product_count_with_empty_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая", "Пустая категория", [])
    assert category.name == "Пустая"
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_multiple_categories_product_count():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("p1", "desc", 10.0, 5)
    Category("Cat1", "Desc", [p1])
    assert Category.product_count == 1

    Category("Cat2", "Desc", [p1])
    assert Category.product_count == 2
