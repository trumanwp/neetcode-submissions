class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0

        while r < n:
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1

        return l







# 2 pointers
# r and l, r is read l is write
# r scans the array
# l tracks the position to write the next unique integer