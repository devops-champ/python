products = {
    "product1": {
        "brand": "A",
        "price": 5.40
    },
    "product2": {
        "brand": "B",
        "price": 7.35
    },
    "product3": {
        "brand": "C",
        "price": 2.24
    }
}


for product, value in products.items():
    print(f"Product: {product}")
    for category, data in value.items():
        print(f"{category}: {data}")