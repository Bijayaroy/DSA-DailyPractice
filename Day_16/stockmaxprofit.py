def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

user_input = input("Enter prices separated by spaces: ")
prices = list(map(int, user_input.split()))

result = max_profit(prices)
print("Maximum profit:", result)
