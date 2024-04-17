products = {}

while True:
    product_name = input("Enter the product name (or 'done' to finish): ")
    if product_name.lower() == 'done':
        break
   
    product_price = float(input("Enter the price: "))
    products[product_name] = product_price




while True:
    search_product = input("Enter a product name to search for its price (or 'done' to exit): ")
    if search_product.lower() == 'done':
        break
   
    if search_product in products:
        print(f"The price of {search_product} is ${products[search_product]:.2f}")
    else:
        print(f"{search_product} is not found in the dictionary.")
