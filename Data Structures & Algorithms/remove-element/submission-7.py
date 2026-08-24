class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        
        



# 2 Pointer
# index i, read pointer, iterating through nums
# index k, write pointer, store positions of wanted values

# iterate through nums
# if nums[i] != val, then we will replace nums[i] with nums[k] and k++

# e.g. [1, 2, 3, 2, 5], val = 2
#    -> nums[0] , i[0], k[0] , "1" is going to be kept, [k] = [i], k++,
#    -> nums [1], i[1], k[1], "2" is going to be discarded, k index remains, no array changes
#    -> nums [2], i[2], k[1], "3" is going to be kept , [k] = [i], k++
# result , [1, 3, 3, 2, 5]