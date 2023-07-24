from menu import products
from management.tab_handler import calculate_tab
from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report, add_product_extra


def main():
    table_1 = [{"_id": 2, "amount": 8}, {"_id": 10, "amount": 4}]
    table_2 = [
        {"_id": 11, "amount": 5},
        {"_id": 22, "amount": 1},
        {"_id": 31, "amount": 4},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    print(menu_report())

    required_keys = ("description", "price", "rating", "title", "type")
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }

    print(add_product(products, **new_product))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
    }
    print(add_product([], **new_product))

if __name__ == "__main__":
    main()
