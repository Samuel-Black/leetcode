from typing import List
from collections import defaultdict

class ValidWordAbbr:

  def __init__(self, dictionary: List[str]):
    self.dict = defaultdict(lambda:{})
    
    for word in dictionary:
      self.dict[self.abbreviate(word)][word] = word

  def isUnique(self, word: str) -> bool:
    return self.dict[self.abbreviate(word)].keys() == {} or (len(self.dict[self.abbreviate(word)].keys()) == 1 and self.dict[self.abbreviate(word)].get(word) == word)
        
  def abbreviate(self, word: str) -> str:
    n = len(word)
    if n <= 2:
      return word
    return word[0] + str(n - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["deer","door","cake","card"])
# obj = ValidWordAbbr(["deer","door","cake","card"])
print(obj.isUnique("dear"))
print(obj.isUnique("cart"))
print(obj.isUnique("cane"))
print(obj.isUnique("make"))
print(obj.isUnique("cake"))
# param_1 = obj.isUnique(word)