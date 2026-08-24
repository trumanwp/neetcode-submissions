from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums is array of numbers
        # k is the desired return of top numbers
        # if k = 2, need to return the 2 numbers that appear the most in nums

        # counter will make the value map
        # use the most_common() method to extract the key:value pairs of k highest
        # loop through result (comes in form of [(1, 3), (2,2)]) 
        # append the first index (the number itself) to the result list
    
        result = []
        # counter = Counter(nums)

        count = Counter(nums).most_common(k)

        for i in count:
            result.append(i[0])
        
        return result