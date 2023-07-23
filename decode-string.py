class Solution:
  def decodeString(self, s: str) -> str:
    
    # characters = set([
    #   "a","A",
    #   "b","B",
    #   "c","C",
    #   "d","D",
    #   "e","E",
    #   "f","F",
    #   "g","G",
    #   "h","H",
    #   "i","I",
    #   "j","J",
    #   "k","K",
    #   "l","L",
    #   "m","M",
    #   "n","N",
    #   "o","O",
    #   "p","P",
    #   "q","Q",
    #   "r","R",
    #   "s","S",
    #   "t","T",
    #   "u","U",
    #   "v","V",
    #   "w","W",
    #   "x","X",
    #   "y","Y",
    #   "z","Z"
    # ])
    
    digits = set()
    for i in range(0, 10):
      digits.add(str(i))
    
    i = 0
    n = len(s)
    res = ""
    while i < n:
      if s[i] in digits:
        multiplier = ""
        while s[i] in digits and s[i] != "[":
          multiplier+=s[i]
          i+=1
        multiplier = int(multiplier)
        i+=1
        string=""
        while s[i] != "]":
          string+=s[i]
          i+=1
        i+=1
        for j in range(0, multiplier):
          res+=string
        # stack = []
      else:
        res+=s[i]
        i+=1
      
    return res
    # for char in s:
      
    
solution = Solution()
print(solution.decodeString("3[a]2[bc]"))
print(solution.decodeString("3[a2[c]]"))
print(solution.decodeString("2[abc]3[cd]ef"))