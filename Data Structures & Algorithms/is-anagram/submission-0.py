class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings, s and t
        # return true if s and t are anagrams
        # anagram means both strings contain the same characters just rearranged

        return sorted(s) == sorted(t)