class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(c for c in s if c.isalnum()).lower()
        l,r = 0, len(new)-1

        while l < r:
            if new[l] == new[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

            