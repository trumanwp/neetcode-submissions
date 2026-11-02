class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        used = [False] * len(nums)
        nums.sort()

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                subset.append(nums[i])
                used[i] = True

                dfs()

                subset.pop()
                used[i] = False
        
        dfs()
        return res
        