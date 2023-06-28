class Solution:
  def reverseWords(self, s: str) -> str:
    res = ""
    
    count = len(s) - 1
    while count >= 0:
      word = ""
      if s[count] != " ":
        while count >= 0 and s[count] != " ":
          word = s[count] + word
          count-=1
        if word != "":
          res+= " " + word
      else:
        count-=1
    return res[1:]
    # arr = []
    #   # count+=1
    # for i in range(len(s), -1, -1):
    #   if s[i] != " ":
    #     res = res + s[i]
      # elif s[i] == " " and : 
    
solution = Solution()
print(solution.reverseWords("  hello world  "))