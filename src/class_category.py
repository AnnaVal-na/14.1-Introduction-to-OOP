from src.class_product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products: list[Product] = []  # Явная аннотация типа
        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его "
                "наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:  # Добавлена аннотация возвращаемого типа
        return "\n".join(
            [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
             for p in self.__products]
        )
