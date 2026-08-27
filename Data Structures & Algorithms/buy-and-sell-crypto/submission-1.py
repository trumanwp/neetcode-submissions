class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        lowest = prices[0]
        
        for num in prices:
            if num < lowest:
                lowest = num
            elif num > lowest:
                res = max(res, num - lowest)
        return res  




