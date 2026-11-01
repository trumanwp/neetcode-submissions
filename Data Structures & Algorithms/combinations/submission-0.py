class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        nums = list(range(1,n + 1))

        def dfs(i):
            if len(subset) == k:
                res.append(subset.copy())
                return
            
            if i >= len(nums):
                return
        
            # Including cur num
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()


            # Excluding cur num
            dfs(i+1)
        
        dfs(0)
        return res