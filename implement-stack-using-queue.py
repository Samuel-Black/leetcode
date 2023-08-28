from unittest import TestCase

class MyStack:

  def __init__(self):
    self.stack = []

  def push(self, x: int) -> None:
    self.stack.append(x)

  def pop(self) -> int:
    val = self.stack[-1]
    del self.stack[-1]
    return val

  def top(self) -> int:
    return self.stack[-1]

  def empty(self) -> bool:
    return not self.stack

solution = MyStack()
test = TestCase()

solution.push(1)
solution.push(2)

test.assertEqual(solution.stack, [1,2])
test.assertEqual(solution.top(), 2)
test.assertEqual(solution.pop(), 2)
test.assertEqual(solution.empty(), False)
test.assertEqual(solution.stack, [1])
