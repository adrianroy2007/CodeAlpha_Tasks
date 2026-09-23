# Stock Portfolio Tracker

print("===== Stock Portfolio Tracker =====")

# Ask the user how they want to define stock names and prices
choice = input(
    "\nDo you want to use predefined stock names and prices "
    "or define your own? (predefined/own): "
).lower()

# Predefined stock prices
if choice == "predefined":
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 420,
        "GOOGL": 165,
        "AMZN": 190
    }

    print("\nUsing predefined stock prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

# User defines their own stock names and prices
elif choice == "own":
    stock_prices = {}

    num_stocks = int(input("\nHow many stocks do you want to define? "))

    for i in range(num_stocks):
        stock = input(f"Enter stock name/symbol #{i + 1}: ").upper()
        price = float(input(f"Enter price for {stock}: $"))

        stock_prices[stock] = price

    print("\nYour stock prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

else:
    print("Invalid choice. Please restart the program.")
    exit()


# Portfolio
portfolio = {}
total_investment = 0

# Ask the user how many stocks they want to add
num_stocks = int(input("\nHow many stocks do you want to add to your portfolio? "))

for i in range(num_stocks):

    stock = input(f"\nEnter stock symbol #{i + 1}: ").upper()

    if stock in stock_prices:

        quantity = int(input(f"Enter quantity of {stock}: "))

        portfolio[stock] = quantity

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(
            f"{stock}: {quantity} shares × "
            f"${stock_prices[stock]} = ${investment}"
        )

    else:
        print("Stock not found in the available stock list.")


# Display portfolio
print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    print(
        f"{stock}: {quantity} shares = ${value}"
    )

print(f"\nTotal Investment Value: ${total_investment}")


# Optional file saving
save = input(
    "\nDo you want to save the result to a file? (yes/no): "
).lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("===== Stock Portfolio Summary =====\n\n")

        for stock, quantity in portfolio.items():

            value = stock_prices[stock] * quantity

            file.write(
                f"{stock}: {quantity} shares = ${value}\n"
            )

        file.write(
            f"\nTotal Investment Value: ${total_investment}\n"
        )

    print("Portfolio saved successfully to portfolio.txt")