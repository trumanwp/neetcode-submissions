class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given a list of numbers (nums)
        # return true if any number appears more than once
        # else return false

        if len(nums) == len(set(nums)):
            return False
        else:
            return True

        

        