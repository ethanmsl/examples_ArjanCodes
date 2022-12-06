"""Ecommerce modeling with dataclass example."""

from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class Customer:
    """Customer's information"""

    name: str
    city: str
    country: str


@dataclass
class Product:
    """Product in ecommerce chart."""

    name: str
    category: str
    shipping_weight: float
    unit_price: float
    tax_percent: float


@dataclass
class Order:
    """Order in ecommerce website."""

    date: date
    status: str
    customer: Customer
    products: List[Product] = field(default_factory=list)

    def add_item(self, product: Product):
        """Insert one product into order."""
        self.products.append(product)

    def calculate_sub_total(self):
        """Total order price without taxes."""
        subtotal = sum((p.unit_price for p in self.products))
        return round(subtotal, 2)

    def calculate_tax(self):
        """Total paid in taxes."""
        taxes = sum((p.unit_price * p.tax_percent for p in self.products))
        return round(taxes, 2)

    def calculate_total(self):
        """Total order price considering taxes."""
        total = self.calculate_sub_total() + self.calculate_tax()
        return round(total, 2)

    @property
    def total_weight(self):
        """Total weight of order."""
        return sum((p.shipping_weight for p in self.products))


if __name__ == "__main__":
    henry = Customer("Henrique", "Sao Jose do Rio Preto", "Brazil")

    banana = Product(
        name="banana",
        category="fruit",
        shipping_weight=0.5,
        unit_price=2.15,
        tax_percent=0.07,
    )

    mango = Product(
        name="mango",
        category="fruit",
        shipping_weight=2,
        unit_price=3.19,
        tax_percent=0.11,
    )

    order = Order(date=date.today(), status="openned", customer=henry)

    order.add_item(banana)
    order.add_item(mango)

    print(f"Total order price: U$ {order.calculate_total()}")
    print(f"Subtotal order price: U$ {order.calculate_sub_total()}")
    print(f"Value paid in taxes: U$ {order.calculate_tax()}")
    print(f"Total weight order: {order.total_weight}")
