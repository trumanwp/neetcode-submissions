class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length = len(nums)
        i = 0

        while i < length:
            if nums[i] == val:
                # starting from this index, all following numbers are equal to the next index, nums[1] becomes nums[2]...
                for j in range(i, length - 1):
                    nums[j] = nums[j+1]
                length -= 1
            else:
                i += 1
            
        return length










        # k = 0
        
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         k += 1

        
        # return k
        


        