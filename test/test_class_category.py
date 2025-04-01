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


def test_add_non_product_object():
    Category.product_count = 0
    category = Category("Тест", "Тест", [])

    class FakeProduct:
        pass  # Создаем класс-пустышку

    fake = FakeProduct()  # Экземпляр не наследуется от Product

    try:
        category.add_product(fake)
        assert False, "Должно было возникнуть исключение TypeError"
    except TypeError as e:
        assert str(e) == (
            "Можно добавлять только объекты Product или его наследников"
        )
        assert Category.product_count == 0  # Счетчик не должен измениться


def test_add_product_subclass():
    # Создаем наследника Product
    class DiscountedProduct(Product):
        def __init__(self, *args, discount=0.1, **kwargs):
            super().__init__(*args, **kwargs)
            self.discount = discount

    product = DiscountedProduct("Со скидкой", "Товар", 1000.0, 5)
    category = Category("Акции", "Спецпредложения", [])

    try:
        category.add_product(product)
        assert "Со скидкой" in category.products
        assert Category.product_count == 1  # Счетчик должен увеличиться
    except TypeError:
        assert False, "Наследники Product должны добавляться корректно"
