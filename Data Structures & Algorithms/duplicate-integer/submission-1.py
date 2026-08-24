class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # list of ints
        # list -> set
        # size of list == set, false

        return len(nums) != len(set(nums))
        