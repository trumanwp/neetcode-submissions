class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        types = { 
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c not in types:
                stack.append(c)
            else:
                if stack and stack[-1] == types[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False






    # Input "[]{}()" - Valid   - stack = [{(
    # Input "[{()}]" - Valid
    # Input "[({)}]" - Invalid

    # Approach - 
    # Remove valid brackets from centre
    # Does string contain "[]", "{}", "()"
    # If it does, remove it / replace with empty string ""
    # Return True if string is empty at end, False if not
    


