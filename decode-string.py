class Solution:
  def decodeString(self, s: str) -> str:

    n = len(s)
    stack = []
    digits = set([str(x) for x in range(0, 10)])
    
    for i in range(0, n):
      if s[i] == "]":
        curr = stack.pop()
        string = ""
        while curr != "[":
          string = curr + string
          curr = stack.pop()
        multiplier = ""
        while stack and stack[-1] in digits:
          multiplier = stack.pop() + multiplier
        multiplier = int(multiplier)
        for j in range(0, multiplier):
          stack.append(string)
      elif s[i] != "]":
        stack.append(s[i])
    return "".join(stack)
    # digits = set()
    # for i in range(0, 10):
    #   digits.add(str(i))
    
    # i = 0
    # n = len(s)
    # res = ""
    # while i < n:
    #   if s[i] in digits:
    #     multiplier = ""
    #     while s[i] in digits and s[i] != "[":
    #       multiplier+=s[i]
    #       i+=1
    #     multiplier = int(multiplier)
    #     i+=1
    #     string=""
    #     while s[i] != "]":
    #       string+=s[i]
    #       i+=1
    #     i+=1
    #     for j in range(0, multiplier):
    #       res+=string
    #     # stack = []
    #   else:
    #     res+=s[i]
    #     i+=1
      
    # return res
    # for char in s:
      
    
solution = Solution()
print(solution.decodeString("3[a]2[bc]"))
print(solution.decodeString("3[a2[c]]"))
print(solution.decodeString("2[abc]3[cd]ef"))