class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = 0
        maxSeq = 0

        for num in numbers:

            if num - 1 not in numbers:
                count = 1
                current = num

                while current + 1 in numbers:
                    count += 1
                    current += 1
        
            maxSeq = max(maxSeq, count)
            count = 0
        
        return maxSeq