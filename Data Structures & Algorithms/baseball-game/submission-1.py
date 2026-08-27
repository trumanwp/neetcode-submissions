class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        - operations are strings that can be
            - an integer, which records a score
            - "+" which records a new score thats the sum of the previous 2 scores
            - "D" which records a new score double that of the last one
            - "C", deletes the previous score
        """
        
        stack, res = [], 0 

        for op in operations:
            if op == "+":
                res += (stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
                
            elif op == "D":
                res += (stack[-1] * 2)
                stack.append(stack[-1] * 2)
                
            elif op == "C":
                res -= stack[-1]
                stack.pop(-1)
            else:
                stack.append(int(op))
                res += int(op)
        
        return res
            