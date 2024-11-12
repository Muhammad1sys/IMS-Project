# Import the utility functions for validation and formatting
from utils import validate_price, validate_quantity, format_price

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity, currency="PKR"):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.currency = currency

        # Use the validate_price function to ensure the price is valid
        self.price = validate_price(price)
        self.stock_quantity = validate_quantity(stock_quantity)  # Validate stock quantity

    def update_stock(self, quantity):
        # Validate quantity to ensure it's a valid number
        new_quantity = self.stock_quantity + quantity
        if new_quantity < 0:
            print("Cannot reduce stock below zero.")
        else:
            self.stock_quantity = new_quantity

    def to_dict(self):
        # Format the price using the format_price function
        formatted_price = format_price(self.price)
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": f"{formatted_price} {self.currency}",  # Format price with currency
            "stock_quantity": self.stock_quantity
        }

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        # Ensure that product is valid before adding
        if product.product_id in self.products:
            print(f"Product with ID {product.product_id} already exists.")
        else:
            self.products[product.product_id] = product

    def delete_product(self, product_id):
        # Check if product exists before deleting
        if product_id in self.products:
            del self.products[product_id]
        else:
            print(f"Product with ID {product_id} not found.")

    def get_product(self, product_id):
        return self.products.get(product_id)

    def get_all_products(self):
        return list(self.products.values())
