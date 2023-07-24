class Solution:
  def isValid(self, s: str) -> bool:
    
    stack = []
    
    opening = set(["(", "[", "{"])
    valid = {
      ")": "(",
      "]": "[",
      "}": "{",
    }
    
    for char in s:
      if char in opening:
        stack.append(char)
      else:
        if len(stack) <= 0:
          return False
        elif valid[char] != stack[-1]: 
          return False
        else:
          stack.pop()
          
    return False if stack else True
solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))