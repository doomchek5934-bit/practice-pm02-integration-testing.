def calculate_price(quantity, unit_price):
    if quantity < 0 or unit_price < 0:
        raise ValueError("Values cannot be negative")
    return quantity + unit_price
