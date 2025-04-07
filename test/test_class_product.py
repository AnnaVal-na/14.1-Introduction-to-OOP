from src.class_product import Product, Smartphone, LawnGrass


def test_product_initialization():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.price == 50000.0


def test_price_validation():
    product = Product("Test", "Test", 100.0, 1)
    product.price = -50
    assert product.price == 100.0


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
        assert str(e) == "Нельзя складывать товары разных классов"


def test_smartphone_creation():
    phone = Smartphone(
        name="iPhone 15",
        description="Флагман",
        price=999.99,
        quantity=10,
        efficiency="A15 Bionic",
        model="15 Pro",
        memory="256GB",
        color="Black"
    )
    assert phone.memory == "256GB"
    assert isinstance(phone, Product)


def test_lawn_grass_creation():
    grass = LawnGrass(
        name="Green Lawn",
        description="Трава",
        price=50.0,
        quantity=100,
        country="Russia",
        germination_period="14 дней",
        color="Green"
    )
    assert grass.country == "Russia"
    assert isinstance(grass, Product)


def test_invalid_addition_diff_classes():
    phone = Smartphone("Phone", "Desc", 100.0, 1, "A", "X", "128GB", "Black")
    grass = LawnGrass("Grass", "Desc", 50.0, 2, "RU", "14d", "Green")

    try:
        phone + grass
        assert False
    except TypeError as e:
        assert str(e) == "Нельзя складывать товары разных классов"
