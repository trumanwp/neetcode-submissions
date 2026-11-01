class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            # Including cur num
            if total + nums[i] <= target:
                subset.append(nums[i])
                dfs(i, total + nums[i])
                subset.pop()

            # Excluding cur num
            dfs(i+1, total)
        
        dfs(0, 0)
        return res