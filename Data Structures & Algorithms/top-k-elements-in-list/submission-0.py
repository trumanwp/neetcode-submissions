from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums is array of numbers
        # k is the desired return of top numbers
        # if k = 2, need to return the 2 numbers that appear the most in nums

        # idea

        # counter will make the value map
        # want to sort the values with their keys#
        # create a result list, loop k times through map to append 

        result = []
        counter = Counter(nums)

        count = counter.most_common(k)

        for i in count:
            result.append(i[0])
        
        return result