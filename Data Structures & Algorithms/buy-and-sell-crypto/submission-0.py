class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price,min_price,profit=prices[0],prices[0],0
        for i in prices:
            if i<min_price:
                profit=max((max_price-min_price),profit)
                min_price=i
                max_price=i
            elif i>max_price:
                max_price=i
        profit=max((max_price-min_price),profit)
        return profit