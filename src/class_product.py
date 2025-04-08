from abc import ABC, abstractmethod


class ReprMixin:
    def __repr__(self):
        args = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({args})"


class BaseProduct(ABC):
    @abstractmethod
    def __init__(
            self, name: str,
            description: str,
            price: float,
            quantity: int
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:  # Добавлен базовый __str__
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    @abstractmethod
    def price(self) -> float: ...

    @price.setter
    @abstractmethod
    def price(self, value: float): ...


class Product(BaseProduct, ReprMixin):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int
    ):
        super().__init__(name, description, price, quantity)
        print(f"Создан {self.__class__.__name__}: {repr(self)}")

    @property
    def price(self) -> float:
        return self._BaseProduct__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._BaseProduct__price = value

    def __add__(self, other: 'Product') -> float:
        if type(self) is not type(other):  # Исправлено на is not
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(
            self, name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
