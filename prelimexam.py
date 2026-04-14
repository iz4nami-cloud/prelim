def get_price_category(price):
    
    if price < 50:
        return "Budget"
    elif price < 200:
        return "Mid-range"
    else:
        return "Premium"


def check_stock_level(stock):
    
    if stock >= 10:
        return "OK"
    else:
        return "LOW STOCK - Reorder needed"


def save_product(name, price, category, stock, stock_status):
    
    with open("inventory.txt", "a") as file:
        file.write(f"Product: {name} | Price: {price:.2f} | Category: {category} | Stock: {stock} | Status: {stock_status}\n")



while True:
    name = input("Enter product name: ")
    price = float(input("Enter product price (in pesos): "))
    stock = int(input("Enter quantity in stock: "))

    category = get_price_category(price)
    stock_status = check_stock_level(stock)

    print("\nPrice Category:", category)
    print("Stock Status:", stock_status)

    save_product(name, price, category, stock, stock_status)
    print("Product saved to inventory!\n")

    choice = input("Add another product? (yes/no): ").lower()
    if choice != "yes":
        print("Inventory update complete. Goodbye!")
        break