from src.class_category import Category
from src.class_product import Product, Smartphone


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


def test_category_str():
    p1 = Product("A", "Desc", 100.0, 2)
    p2 = Product("B", "Desc", 200.0, 3)
    category = Category("Test", "Desc", [p1, p2])
    assert str(category) == "Test, количество продуктов: 5 шт."


def test_empty_category_str():
    category = Category("Empty", "Desc", [])
    assert str(category) == "Empty, количество продуктов: 0 шт."


def test_add_invalid_product_type():
    category = Category("Test", "Desc", [])

    try:
        category.add_product("Not a product")
        assert False
    except TypeError as e:
        assert "только продукты" in str(e)


def test_add_valid_subclass():
    phone = Smartphone("Phone", "Desc", 100.0, 1, "A", "X", "128GB", "Black")
    category = Category("Tech", "Gadgets", [])

    try:
        category.add_product(phone)
        assert len(category.products.split('\n')) == 1
    except TypeError:
        assert False
