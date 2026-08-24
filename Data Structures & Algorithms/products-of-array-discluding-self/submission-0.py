class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        current = 0
        temp = 0

        for num in nums:
            temp = num
            nums.pop(current)     

            prod = 1
            for x in nums:
                prod *= x 
            
            answer.append(prod)
            nums.insert(current,temp)   
            current += 1
        
        return answer