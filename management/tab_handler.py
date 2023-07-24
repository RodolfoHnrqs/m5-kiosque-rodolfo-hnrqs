from menu import products
from .product_handler import get_product_by_id


def calculate_tab(consumptions):
    subtotal = 0
    for product_item in consumptions:
        product = get_product_by_id(product_item["_id"])
        subtotal += product["price"] * product_item["amount"]
    subtotal = str(round(subtotal, 2))
    return {"subtotal": f'${subtotal}'}
