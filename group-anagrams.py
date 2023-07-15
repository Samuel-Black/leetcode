import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = collections.defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    
    # dict = {}
    
    # for s in strs:
    #   key = len(s)
    #   # temp = int(s)
    #   for c in s:
    #     key += ord(c) - 96
    #   # exp = 10
    #   # while temp % exp > 0:
    #   #   key += temp % exp
    #   #   temp //= exp
    #   if dict.get(key):
    #     dict[key].append(s)
    #   else:
    #     dict[key]=[s]
        
    # return list(dict.values())
    
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))