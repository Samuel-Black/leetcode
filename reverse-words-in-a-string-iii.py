class Solution:
  def reverseWords(self, s: str) -> str:
    
    stack = []
    i = 0
    n = len(s)
    res = ""
    while i < n:
      reversedStr = ""
      while i < n and s[i] != " ":
        reversedStr = s[i] + reversedStr
        i+=1
      if reversedStr != "":
        res += reversedStr
        continue
      elif i < n:
        res += s[i]
      i+=1
    return res
    
    # res = ""
    # count = len(s) - 1
    # while count >= 0:
    #   word = ""
    #   while count >= 0 and s[count] != " ":
    #     word += s[count]
    #     count-=1
    #   if word != "":
    #     res = word + res
    #   else:
    #     res = s[count] + res
    #     count-=1
      
    # return res
    
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))