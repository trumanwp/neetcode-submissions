class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        array "prices", prices[i] is the price of neetcoin on ith day

        choose a single day to buy a coin, and a different day in the future to sell it

        return the max profit you can achieve

        you can choose to not make any transactions in which case the profit would be 0

        --

        sliding window

        store maxResult = 0
        l = 0, 

        while l < len(prices):
            r = l + 1
            while r<= len(prices)

            calculate r - l, if is greater than maxResult, maxresult = r-l

            iterate r
        
        iterate l
        """

        maxResult = 0
        l = 0

        while l < len(prices) - 1:
            r = l + 1
            while r <= len(prices) - 1:
                maxResult = max(maxResult, prices[r] - prices[l])
                r += 1
            l += 1
        
        return maxResult

