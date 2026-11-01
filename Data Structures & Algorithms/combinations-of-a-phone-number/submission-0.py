class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        - backtracking
        - make a map of nums to chars
        - create dfs function that takes an index and a current substring
        - base cases - if the length of substring is equal to length of digits, 
          append substring  to res
        - then
        - loop through the characters of each digit using the map
        - for each character, run the recursive call, incrementing index by 1, 
           and adding char to current substring
        - call function with index of 0 and "" if digits are present
        """

        res = []
        

        numToChars = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
            }

        def dfs(i, current):
            if len(current) == len(digits):
                res.append(current)
                return
            
            for char in numToChars[digits[i]]:
                dfs(i+1, current + char)
            
        if digits:
            dfs(0, "")
        
        return res

        
                

            