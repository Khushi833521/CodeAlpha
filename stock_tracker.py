
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/AMZN): ").upper()
quantity = int(input("Enter quantity: "))


if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_value = price * quantity

    print("\n📊 Portfolio Summary")
    print("Stock:", stock_name)
    print("Price per stock:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total_value)

    with open("portfolio.txt", "a") as file:
        file.write(f"{stock_name}, {quantity}, {total_value}\n")

    print("\n✅ Data saved in portfolio.txt")

else:
    print("❌ Stock not found!")
