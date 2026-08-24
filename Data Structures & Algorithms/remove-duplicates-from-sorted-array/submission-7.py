class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []

        for i in nums:
            if i in temp:
                continue
            else:
                temp.append(i)
        
        for j in range(len(temp)):
            nums[j] = temp[j]
            
        
        return len(temp)

# time complexity = O(n^2)
# space complexity = O(n)



# BRUTE FORCE
# create temp list
# iterate through nums, for each number , if number isnt in temp list , add it to the temp list
# this will end with us having no duplicates in the temp list
# merge the temp list onto the original list, with the return (k) = len(temp)

# e.g, nums = [2, 3, 5, 5, 6, 7] -> temp = [2, 3, 5, 6, 7]
#       temp[0] = nums[0] ....