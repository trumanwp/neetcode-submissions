class Solution:
    def isValid(self, s: str) -> bool:

        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        
        return True if not s else False







    # Input "[]{}()" - Valid
    # Input "[{()}]" - Valid
    # Input "[({)}]" - Invalid

    # Approach - 
    # Remove valid brackets from centre
    # Does string contain "[]", "{}", "()"
    # If it does, remove it / replace with empty string ""
    # Return True if string is empty at end, False if not
    


