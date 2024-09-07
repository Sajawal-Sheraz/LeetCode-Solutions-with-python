def maxProfit(prices):
    prev_ptr = 0
    next_ptr = 0
    max_profit = 0
    while next_ptr < len(prices):
        current_profit = prices[next_ptr] - prices[prev_ptr]
        if prices[prev_ptr] < prices[next_ptr]:
            max_profit = max(max_profit, current_profit)
        else:
            prev_ptr = next_ptr
        next_ptr += 1
    return max_profit


prices = [7, 1, 5, 3, 6, 4]


print(maxProfit(prices))
