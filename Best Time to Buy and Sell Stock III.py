class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_total_profit, min_price_so_far = 0, float('inf')
        first_buy_sell_profits = [0] * len(prices)

        # Forward phase

        for i, price in enumerate(prices):
            min_price_so_far = min(min_price_so_far , price)
            max_total_profit = max(max_total_profit , price - min_price_so_far)
            first_buy_sell_profits [i] = max_total_profit
        # Backward phase

        max_price_so_far = float('-inf')
        for i, price in reversed(list(enumerate(prices[1:], 1))): #sell must be at least one day after buy
            max_price_so_far = max(max_price_so_far, price)
            max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i-1])

        return(max_total_profit)