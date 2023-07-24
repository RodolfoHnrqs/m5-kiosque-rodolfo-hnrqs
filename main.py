from menu import products
from management.tab_handler import calculate_tab
from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report, add_product_extra


def main():

    found_product = get_product_by_id(25)
    print(found_product)

    print(get_products_by_type('drink'))

    test_add = add_product(products,
                      description='Concept of healthy breakfast with mesli',
                      price=22.7, rating=2, title='Breakfast with muesli',
                      type='dairy')
    print(test_add)

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
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


if __name__ == "__main__":
    main()
