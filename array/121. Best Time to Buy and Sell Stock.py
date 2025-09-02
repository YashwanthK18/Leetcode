class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0
        for p in prices[1:]:
            if price > p:
                price = p
            if profit < p - price:
                profit = p - price
        return profit
