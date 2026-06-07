class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        print(f"""prices: {prices}""")
        for i, price in enumerate(prices):

            if i == (len(prices) - 1):
                return max_profit
            future_prices = prices[i+1:]
            projected_profit = max(future_prices) - price
            print(f"""max_profit: {max_profit}""")
            print(f"""i: {i}""")
            print(f"""prices[i]: {prices[i]}""")
            print(f"""future_prices: {future_prices}""")
            print(f"""price: {price}""")
            print(f"""projected_profit: {projected_profit}""")
            print("---\n")
            if projected_profit > max_profit:
                max_profit = projected_profit
            print(f"""max_profit: {max_profit}""")
        return max_profit
            
        