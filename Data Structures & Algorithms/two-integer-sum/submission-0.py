class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given an array of numbers (nums)
        # given an integer target (target)
        # return the 2 numbers that add to equal target
        # return must have the smaller number first

        # create a dictionary, that holds all the values we have seen, and their index
        # loop through each value in nums with enumerate, because we need the index for the return
        # for each number, find the "desired" , with target-nums . this gives us the number we need
        # if the desired number is in the dictionary, we can return both numbers 
        # if its not, we add the current number and its index to the dictionary
    
        hashmap = {}

        for i, num in enumerate(nums):
            desired = target - num

            if desired in hashmap:
                return sorted([hashmap[desired] , i])
            else:
                hashmap[num] = i
