class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,v in enumerate(nums):
            desired = target - v

            if desired in hashmap:
                return sorted([hashmap[desired], i])
            
            hashmap[v] = i