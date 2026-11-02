class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def dfs(start, end):
            if start >= len(s):
                res.append(sub.copy())
                return 
            
            if self.isPali(s, start, end):
                sub.append(s[start:end+1])
                dfs(end + 1, end + 1)
                sub.pop()
            
            if end + 1 < len(s):
                dfs(start, end + 1)
                
        dfs(0,0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
        
        