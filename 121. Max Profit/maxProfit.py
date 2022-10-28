# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

def maxProfit(prices: List[int]) -> int:
    lowest = float('inf')
    highest = 0
    for price in prices:
        lowest = min(lowest, price)
        profit = price - lowest
        highest = max(highest, profit)
    return highest
    
    # max = 0
    # for index, value in enumerate(prices):
    #     for value2 in prices[index+1:]:
    #         if value2 - value > max:
    #             max = value2 - value
    # return max

assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
assert maxProfit([2,4,1]) == 2
assert maxProfit([7,1,8]) == 7
assert maxProfit([4,3,3,6,1,9]) == 8
assert maxProfit([2,4,9,7,3,7,9,1,0,6,7,6]) == 7