"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and 
selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock 
at 5 dollars and sell it at 10 dollars.
"""

def max_profit(prices):
    prev_low = prices[0]
    best_profit = 0
    for p in prices:
        best_profit = max(best_profit, p-prev_low)
        prev_low = min(prev_low, p)
    return best_profit

if __name__ == "__main__":
    print(max_profit([1,2,3,4]))
    print(max_profit([4,3,2,1]))
    print(max_profit([9,11,8,5,7,10]))


