from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given an array of strings
        # return all anagrams into sublists
        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # want to loop through each word, add sorted combination of letters as a key in the map
        # want each key to have a set of values in a data structure, of the suitable words
        # return the values

        anagram_map = defaultdict(list)
        result = []

        for s in strs: # adam
            sorted_s = tuple(sorted(s)) # ("a", "a", "d", "m")
            anagram_map[sorted_s].append(s) # {"a", "a", "d", "m" : "adam"}

        for val in anagram_map.values():
            result.append(val)

        return result

