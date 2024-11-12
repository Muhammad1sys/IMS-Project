# products.py
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity


class ProductManager:
    def __init__(self):
        self.products = {}
        self.next_id = 1  # Track the next product ID

    def add_product(self, name, category, price, stock_quantity):
        # Create a new product and assign it an ID
        product = Product(self.next_id, name, category, price, stock_quantity)
        self.products[self.next_id] = product
        self.next_id += 1  # Increment the ID for the next product
        print(f"Product {product.name} added successfully.")

    def view_products(self):
        if self.products:
            print("\nProduct List:")
            for product in self.products.values():
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Stock: {product.stock_quantity}")
        else:
            print("No products found.")

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price:
                product.price = price
            if stock_quantity is not None:  # If quantity is provided, update it (including 0)
                product.stock_quantity = stock_quantity
            print(f"Product {product_id} updated.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} deleted.")
        else:
            print("Product not found.")
