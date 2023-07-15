from typing import List

class Solution:
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    
    def hash(string: str) -> int:
      # number of times for the first character to be shifted to equal 'a'
      shift = ord(string[0])
      digest = ""
      for c in string:
        digest += chr((ord(c) - shift) % 26 + ord('a'))
      return digest
      # return ord(string[0])
    
    dict = {}
    
    for s in strings:
      # n = len(s)
      key = hash(s)
      # for i in range(0, n - 1):
      #   temp = hash(s)
      #   print(chr(temp))
        # key+=abs((ord(s[i]) - 96) - (ord(s[i + 1]) - 96) - 26) % 26
      # key%=50
      if dict.get(key) == None:
        dict[key] = [s]
      else:
        dict[key].append(s)
        
    return list(dict.values())
    
solution = Solution()
print(solution.groupStrings(["cba","abc","bcd","acef","xyz","az","ba","a","z"]))