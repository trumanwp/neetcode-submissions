class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []

        for i in nums:
            if i != val:
                temp.append(i)
        
        for j in range(len(temp)):
            nums[j] = temp[j]
        
        return len(temp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # create a temp list
        # iterate through nums list
        # any numbers that != val, add to the temp list
        # for RETURN = len(temp)
        # for OUTPUT = take the temp list, merge it to the original list, where values beyond nums[len(temp)] dont matter
            # temp[0] = nums[0] ....

        # [1,2,4,4,5], val = 4 -> [1,2,5,4,5]

