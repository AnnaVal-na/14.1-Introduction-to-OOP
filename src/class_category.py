from src.class_product import Product
from typing import List  # Импортируем List для аннотации списка


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self,
                 name: str,
                 description: str,
                 products: List[Product]):
        self.name = name
        self.description = description
        self.__products: List[Product] = []
        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(
            [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
             for p in self.__products]
        )
