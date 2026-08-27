class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        - operations are strings that can be
            - an integer, which records a score
            - "+" which records a new score thats the sum of the previous 2 scores
            - "D" which records a new score double that of the last one
            - "C", deletes the previous score
        """
        
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop(-1)
            else:
                stack.append(int(op))
        
        return sum(stack)
            