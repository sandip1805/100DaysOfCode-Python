class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        greatest_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            greatest_profit = max(prices[i] - lowest_price, greatest_profit)
        return greatest_profit