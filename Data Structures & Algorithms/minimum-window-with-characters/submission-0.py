from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        l = start = end = 0

        for r, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                if end == 0 or r - l + 1 < end - start:
                    start, end = l, r + 1
                
                need[s[l]] += 1

                if need[s[l]] > 0:
                    missing += 1
                l += 1
        
        return s[start:end]
        
