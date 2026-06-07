class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            if i == (len(prices) - 1):
                return max_profit
            future_prices = prices[i+1:]
            projected_profit = max(future_prices) - price
            if projected_profit > max_profit:
                max_profit = projected_profit
            
        