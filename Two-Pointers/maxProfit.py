# The function calculates the maximum profit that can be achieved from a list of stock prices by buying and selling once.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r != len(prices):
            if prices[r] > prices[l]:
                prof = prices[r] - prices[l]
                maxP = max(maxP, prof)

            else:
                l = r

            r += 1

        return maxP