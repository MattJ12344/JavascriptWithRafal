def find_best_days(prices):
    
    min_price = prices[0]
    buy_day = 0
    max_profit = 0
    sell_day = 0

    for i in range(1, len(prices)):
      
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_day = prices.index(min_price)
            sell_day = i

      
        if prices[i] < min_price:
            min_price = prices[i]

    
    return f"{buy_day + 1};{sell_day + 1};{max_profit * 100000}"

with open("tekst.txt", "r") as file:
    prices = list(map(int, file.read().split()))

print(find_best_days(prices))

