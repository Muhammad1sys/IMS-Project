import re

def validate_price(price_input):
    """
    Validates the price input and returns a float value if valid, else returns None.
    Removes currency symbols and commas.
    """
    try:
        # Remove currency symbols and commas, then convert to float
        price = float(price_input.replace('$', '').replace(',', '').strip())
        return price
    except ValueError:
        print("Invalid price input. Please enter a valid numeric value.")
        return None

def validate_quantity(quantity_input):
    """
    Validates that the input quantity is a valid integer.
    Returns the quantity if valid, else returns None.
    """
    try:
        quantity = int(quantity_input)
        if quantity < 0:
            print("Quantity cannot be negative.")
            return None
        return quantity
    except ValueError:
        print("Invalid quantity. Please enter a valid integer.")
        return None

def format_price(price):
    """
    Formats the price to a string with commas as thousand separators and two decimal places.
    """
    return f"{price:,.2f}"
