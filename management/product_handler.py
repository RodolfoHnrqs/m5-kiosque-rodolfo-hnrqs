from menu import products

def get_product_by_id(id: int):
    if not type(id) is int:
        raise TypeError("product id must be an int")
    
    for product in products:
        if product["_id"] == id:
            return product
    return {}

def get_products_by_type(types: str):
    found_results = []

    if not type(types) is str:
        raise TypeError('product type must be a str')
       
    for product in products:
        if product["type"] == types:
            found_results.append(product)
    return found_results

def add_product(menu, **product):
    if len(menu):
        incremental_id = max(product_item['_id'] for product_item in menu)
        product['_id'] = incremental_id + 1
        menu.append(product)
        return product
    product['_id'] = 1
    menu.append(product)
    return product

def menu_report():
    products_quantity = len(products)
    average_price = 0
    commom_types = {}
    for product in products:
        average_price += product["price"] / products_quantity
    types = [types["type"] for types in products]
    for product_item in types:
        commom_types[(product_item)] = types.count(product_item)
    commom_types = max(commom_types, key=commom_types.get)
    return f"Products Count: {products_quantity} - Average Price: ${average_price:.1f} - Most Common Type: {commom_types}"