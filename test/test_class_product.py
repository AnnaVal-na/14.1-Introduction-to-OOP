from src.class_product import Product

# Старые тесты


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.price == 50000.0


def test_price_validation():
    product = Product("Test", "Test", 100.0, 1)
    product.price = -50
    assert product.price == 100.0

# Новые тесты по заданию 3


def test_product_str():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_product_addition():
    p1 = Product("A", "Desc", 100.0, 2)
    p2 = Product("B", "Desc", 200.0, 3)
    assert p1 + p2 == (100*2 + 200*3)


def test_invalid_addition():
    p = Product("Test", "Test", 100.0, 1)
    try:
        p + 100  # Пытаемся сложить с числом
        assert False, "Должно возникать исключение TypeError"
    except TypeError as e:
        assert str(e) == "Можно складывать только объекты Product"
